import path from "path";
import cookie from "@fastify/cookie";
import formBody from "@fastify/formbody";
import staticFiles from "@fastify/static";
import dotenv from "dotenv";
import { clearFlashCookie, FLASH_MSG_COOKIE } from "./flash";
import Fastify from "fastify";

import nunjucks from "nunjucks";
import { z } from "zod";
import { cmpPassword, HashedPassword, hashPassword } from "./auth";

import { connect, newDb, SqliteSession, SqliteUserRepository } from "./db";
import type { FastifyRequest } from "fastify/types/request";
import type { FastifyReply } from "fastify/types/reply";

dotenv.config();
const SESSION_COOKIE = "SESSION_ID";

const envir = process.env.NODE_ENV || "development";
const cookieSecret = process.env.CookieSecret || "secret";
if (cookieSecret === undefined) {
  console.error("CookieSecret is not defined");
  process.exit(1);
}

const template = new nunjucks.Environment(
  new nunjucks.FileSystemLoader("src/backend/templates")
);
const USERS_DB = "./users.sqlite";

const fastify = Fastify({
  logger: true,
});

const accountCreateRequestSchema = z.object({
  email: z.string(),
  password: z.string(),
  agreedToTerms: z.string().optional(),
});

type accountCreateRequest = z.infer<typeof accountCreateRequestSchema>;

const accountLoginRequestSchema = z.object({
  email: z.string(),
  password: z.string(),
  agreedToTerms: z.string().optional(),
});

type accountLoginRequest = z.infer<typeof accountLoginRequestSchema>;
{
  fastify.register(formBody);
  fastify.register(cookie, {
    secret: cookieSecret,
  });
  fastify.register(clearFlashCookie);
  fastify.register(staticFiles, {
    root: path.join(__dirname, "../../dist"),
  });
}

function setFlashCookie(reply: FastifyReply, msg: string): void {
  reply.setCookie(FLASH_MSG_COOKIE, msg, { path: "/" });
}

function readFlashCookie(request: FastifyRequest): string | undefined {
  return request.cookies[FLASH_MSG_COOKIE];
}
function setSesstionCokkie(reply: FastifyReply, sessionId: string): void {
  reply.setCookie(SESSION_COOKIE, sessionId, { path: "/" });
}

function readSessionCookie(request: FastifyRequest): string | undefined {
  return request.cookies[SESSION_COOKIE];
}
fastify.get("/", async (request, reply) => {
  await reply.send("Hi there!");
});

fastify.get("/signup", async (request, reply) => {
  const rendered = template.render("signup.njk", { envir });
  return await reply
    .header("Content-Type", "text/html; charset=utf-8")
    .send(rendered);
});

fastify.post("/account/signup", async (request, reply) => {
  let requestData: accountCreateRequest;
  try {
    requestData = accountCreateRequestSchema.parse(request.body);
  } catch (e) {
    return await reply.redirect("/signup");
  }

  if (requestData.agreedToTerms !== "on") {
    return await reply.redirect("/signup");
  }

  const db = await connect(USERS_DB);
  const userRepository = new SqliteUserRepository(db);
  const hashedPassword = await hashPassword(requestData.password);

  try {
    const newUser = {
      ...requestData,
      id: 0,
      agreedToTerms: true,
      hashedPassword,
    };
    const user = await userRepository.create(newUser);
    const sessions = new SqliteSession(db);
    const sessionId = await sessions.create(user.id);
    setSesstionCokkie(reply, sessionId);
    return await reply.redirect("/welcome");
  } catch (e) {
    return await reply.redirect("/signup");
  }
});

fastify.post("/signin", async (request, reply) => {
  const rendered = template.render("signin.njk", { envir });
  return await reply
    .header("Content-Type", "text/html; charset=utf-8")
    .send(rendered);
});

fastify.post("/account/signin", async (request, reply) => {
  let requestData: accountLoginRequest;
  try {
    requestData = accountLoginRequestSchema.parse(request.body);
  } catch (e) {
    return await reply.redirect("/signin");
  }

  const db = await connect(USERS_DB);
  const userRepository = new SqliteUserRepository(db);
  try {
    const user = await userRepository.findByEmail(requestData.email);
    if (user === undefined) {
      return await reply.redirect("/signin");
    }
    const passwordMatches = await cmpPassword(
      requestData.password,
      user.hashedPassword
    );
    if (!passwordMatches) {
      return await reply.redirect("/signin");
    }
    const sessions = new SqliteSession(db);
    const sessionId = await sessions.create(user.id);
    setSesstionCokkie(reply, sessionId);
    return await reply.redirect("/welcome");
  } catch (e) {
    return await reply.redirect("/signin");
  }
});

const start = async (): Promise<void> => {
  try {
    const db = await connect(USERS_DB);
    newDb(db);
    await fastify.listen({ port: 3000 });
  } catch (error) {
    fastify.console.log(error);
    process.exit(1);
  }
};
start();

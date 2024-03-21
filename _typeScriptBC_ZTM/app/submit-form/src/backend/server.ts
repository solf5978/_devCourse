import path from "path";
import cookie from "@fastify/cookie";
import formBody from "@fastify/formbody";
import staticFiles from "@fastify/static";
import dotenv from "dotenv";
import Fastify from "fastify";
import nunjucks from "nunjucks";
import { z } from "zod";
import { HashedPassword, hashPassword } from "./auth";

import { connect, newDb, SqliteSession, SqliteUserRepository } from "./db";

dotenv.config();
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

{
  fastify.register(formBody);
  fastify.register(cookie, {
    secret: cookieSecret,
  });
  fastify.register(staticFiles, {
    root: path.join(__dirname, "../../dist"),
  });
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
    console.log(user);
    return await reply.redirect("/welcome");
  } catch (e) {
    return await reply.redirect("/signup");
  }
});

fastify.post("/signinp", async (request, reply) => {
  const rendered = template.render("signin.njk", { envir });
  return await reply
    .header("Content-Type", "text/html; charset=utf-8")
    .send(rendered);
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

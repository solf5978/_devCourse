import path from "path";
import cookie from "@fastify/cookie";
import formBody from "@fastify/formbody";
import staticFiles from "@fastify/static";
import dotenv from "dotenv";
import Fastify from "fastify";
import nunjucks from "nunjucks";
import { z } from "zod";

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

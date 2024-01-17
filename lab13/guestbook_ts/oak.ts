import { Application, Router, send } from "https://deno.land/x/oak/mod.ts";
import { MongoClient } from "https://deno.land/x/mongo@v0.32.0/mod.ts";
import {
    dejsEngine,
    oakAdapter,
    viewEngine,
  } from "https://deno.land/x/view_engine/mod.ts";

const app = new Application();
const router = new Router();
const PORT = 8000;

const MONGO_URL = "mongodb://127.0.0.1:27017";
const client = new MongoClient();

// Set up EJS view engine
app.use(viewEngine(oakAdapter, dejsEngine, {viewRoot: "."}));

app.use(async (ctx, next) => {
  await next();
  const rt = ctx.response.headers.get("X-Response-Time");
  console.log(`${ctx.request.method} ${ctx.request.url} - ${rt}`);
});

app.use(async (ctx, next) => {
  const start = Date.now();
  await next();
  const ms = Date.now() - start;
  ctx.response.headers.set("X-Response-Time", `${ms}ms`);
});

app.use(router.routes());
app.use(router.allowedMethods());

router.get("/", async (ctx) => {
  const posts = await getEntries();
  await ctx.render("index.ejs", { posts });
});

router.get("/entries", async (ctx) => {
  const data = await getEntries();
  ctx.response.body = data;
});

router.post("/submit", async (ctx) => {
  const body = await ctx.request.body();
  const { name, content } = body.value;
  console.log(name);
  console.log(content);
  await client.connect(MONGO_URL);
  console.log("Connected correctly to server");
  const db = client.database("guestbook");
  const col = db.collection("entries");
  const data = await col.insertOne({ name, content });
  console.log(data);
  client.close();
  ctx.response.redirect("/");
});

app.addEventListener("listen", ({ hostname, port }) => {
  console.log(`Server is running on http://${hostname}:${port}`);
});

await app.listen({ port: PORT });

async function getEntries() {
  await client.connect(MONGO_URL);
  console.log("Connected correctly to server");
  const db = client.database("guestbook");
  const col = db.collection("entries");
  const data = await col.find().toArray();
  console.log(data);
  return data;
}

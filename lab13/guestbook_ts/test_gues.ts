import express, { Express, Request, Response } from "npm:express@^4";
import morgan from "npm:morgan@^1";
import * as fs from "node:fs";
import * as path from "node:path";
import { MongoClient } from "https://deno.land/x/mongo@v0.32.0/mod.ts";

const app: Express = express();
const PORT: number = 8000;

const MONGO_URL: string = "mongodb://127.0.0.1:27017";
const client = new MongoClient();

app.use(morgan("dev"));
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.get("/", (req: Request, res: Response) => {
  const htmlContent = fs.readFileSync(
    path.join(path.resolve(), "index.html"),
    "utf-8",
  );
  res.send(htmlContent);
});

app.get("/entries", async (req: Request, res: Response) => {
  await client.connect(MONGO_URL);
  console.log("Connected correctly to server");
  const db = client.database("guestbook");
  const col = db.collection("entries");
  const data = await col.find().toArray();
  console.log(data);
  res.json(data);
});

app.post("/submit", async (req: Request, res: Response) => {
  const body = req.body;
  const name: string = body.name;
  const content: string = body.content;
  console.log(name);
  console.log(content);
  await client.connect(MONGO_URL);
  console.log("Connected correctly to server");
  const db = client.database("guestbook");
  const col = db.collection("entries");
  const data = await col.insertOne({ name: name, content: content });
  console.log(data);
  client.close();
  res.redirect("/");
});


app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
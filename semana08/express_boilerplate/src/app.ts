import express from "express";
import dotenv from "dotenv";

dotenv.config();

import { connectToMongo } from "./config/mongodb";

const main = () => {
  const app = express();
  const PORT = +process.env.PORT! || 8000;

  app.get("/", (req, res) => {
    res.send("Welcome to the Express server! 😎");
  });

  app.get("/customers", async (req, res) => {
    const db = await connectToMongo();
    const collection = db.collection("customers");
    const customers = await collection.find().toArray();

    res.json({
      ok: true,
      object: "customers_list",
      data: customers
    });
  });

  app.listen(PORT);
  console.log(`Server is running on: http://localhost:${PORT}`);
};

main();

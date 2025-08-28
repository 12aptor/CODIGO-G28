import { MongoClient, Db } from "mongodb";

let db: Db;

export const connectDB = async () => {
  if (db) {
    return db;
  }

  const uri = process.env.MONGODB_URI;
  if (!uri) {
    throw new Error("MONGODB_URI is not defined");
  }

  const client = new MongoClient(uri);
  await client.connect();
  db = client.db();
  return db;
};

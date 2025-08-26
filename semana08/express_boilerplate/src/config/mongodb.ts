import { MongoClient } from "mongodb";

export const connectToMongo = async () => {
  const uri = process.env.MONGODB_URI;
  console.log("MONGODB_URI:", uri);
  if (!uri) {
    throw new Error("MONGODB_URI is not defined in environment variables");
  }
  const client = new MongoClient(uri);
  const db = client.db("ecommerce");
  return db;
};

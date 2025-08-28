import type { Request, Response } from "express";
import { connectDB } from "../config/mongodb";
import { messageSchema } from "../schemas/message.schema";
import { ObjectId } from "mongodb";

export const getMessages = async (req: Request, res: Response) => {
  try {
    const channelId = req.params.channelId;
    const db = await connectDB();
    const collection = db.collection("messages");
    const messages = await collection
      .find({
        channelId: channelId,
      })
      .toArray();

    res.status(200).json({
      ok: true,
      object: "list_messages",
      data: messages,
    });
    return;
  } catch (error) {
    if (error instanceof Error) {
      res.status(400).json({
        ok: false,
        object: "list_messages",
        error: error.message,
      });
      return;
    }
  }
};

export const createMessage = async (req: Request, res: Response) => {
  try {
    const authorId = req.userId!;
    const data = await messageSchema.parseAsync(req.body);

    const db = await connectDB();
    const collection = db.collection("messages");

    const userCollection = db.collection("users");
    const user = await userCollection.findOne({
      _id: new ObjectId(authorId),
    });

    if (!user) {
      throw new Error("User not found");
    }

    const message = await collection.insertOne({
      ...data,
      createdAt: new Date(),
      author: {
        id: authorId,
        name: user.name,
        email: user.email,
      },
    });

    const createdMessage = await collection.findOne({
      _id: message.insertedId,
    });

    res.status(200).json({
      ok: true,
      object: "create_message",
      data: createdMessage,
    });
    return;
  } catch (error) {
    if (error instanceof Error) {
      res.status(400).json({
        ok: false,
        object: "create_message",
        error: error.message,
      });
    }
  }
};

import type { Request, Response } from "express";
import { channelSchema } from "../schemas/channel.schema";
import { ZodError } from "zod";
import { connectDB } from "../config/mongodb";

export const getChannels = async (req: Request, res: Response) => {
  try {
    const db = await connectDB();
    const collection = db.collection("channels");
    const channels = await collection.find().toArray();

    res.status(200).json({
      ok: true,
      object: "list_channels",
      data: channels,
    });
    return;
  } catch (error) {
    if (error instanceof Error) {
      res.status(400).json({
        ok: false,
        object: "list_channels",
        error: error.message,
      });
      return;
    }
  }
};

export const createChannel = async (req: Request, res: Response) => {
  try {
    const data = await channelSchema.parseAsync(req.body);

    const db = await connectDB();
    const collection = db.collection("channels");

    const channel = await collection.insertOne(data);

    const createdChannel = await collection.findOne({
      _id: channel.insertedId,
    });

    res.status(200).json({
      ok: true,
      object: "create_channel",
      data: createdChannel,
    });
    return;
  } catch (error) {
    if (error instanceof ZodError) {
      res.status(400).json({
        ok: false,
        object: "list_channels",
        error: error.issues,
      });
      return;
    } else if (error instanceof Error) {
      res.status(400).json({
        ok: false,
        object: "list_channels",
        error: error.message,
      });
      return;
    }
  }
};

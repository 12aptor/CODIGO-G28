import type { Request, Response } from "express";
import { channelSchema } from "../schemas/channel.schema";
import { ZodError } from "zod";
import { connectToMongo } from "../config/mongodb";

export const getChannels = async (req: Request, res: Response) => {
  try {
    const db = await connectToMongo();
    const collection = db.collection("channels");
    const channels = await collection.find().toArray();

    res.status(200).json({
      ok: true,
      object: "list_channels",
      data: channels,
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

import { Server } from "socket.io";
import type { Server as HttpServer } from "http";
import { connectDB } from "./mongodb";
import { ObjectId } from "mongodb";

let io: Server;

export const initSocket = (server: HttpServer): Server => {
  io = new Server(server, {
    cors: {
      origin: "*",
      methods: ["GET", "POST"],
    },
  });

  io.on("connection", (socket) => {
    socket.on("message", async (data) => {
      try {
        const db = await connectDB();
        const collection = db.collection("messages");

        const userCollection = db.collection("users");
        const user = await userCollection.findOne({
          _id: new ObjectId(data.author_id),
        });

        if (!user) {
          throw new Error("User not found");
        }

        const message = await collection.insertOne({
          content: data.content,
          createdAt: new Date(),
          channelId: data.channel_id,
          author: {
            id: data.author_id,
            name: user.name,
            email: user.email,
          },
        });

        const createdMessage = await collection.findOne({
          _id: message.insertedId,
        });

        io.emit("message", createdMessage);
      } catch (error) {
        console.log("Error handling message", error);
      }
    });
  });

  return io;
};

import express from "express";
import dotenv from "dotenv";
import { createServer } from "http";

dotenv.config();

import { authRouter } from "./routes/auth.router";
import { channelRouter } from "./routes/channel.router";
import { messageRouter } from "./routes/message.router";
import { authMiddleware } from "./config/middleware";
import { initSocket } from "./config/socket";

const main = () => {
  const app = express();
  const PORT = +process.env.PORT! || 8000;
  const server = createServer(app);

  initSocket(server);

  app.use(express.json());

  app.use("/api/auth", authRouter);
  app.use("/api/channels", authMiddleware, channelRouter);
  app.use("/api/messages", authMiddleware, messageRouter);

  server.listen(PORT);
  console.log(`Server is running on: http://localhost:${PORT}`);
};

main();

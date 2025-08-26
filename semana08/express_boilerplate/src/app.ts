import express from "express";
import dotenv from "dotenv";

dotenv.config();

import { authRouter } from "./routes/auth.router";

const main = () => {
  const app = express();
  const PORT = +process.env.PORT! || 8000;

  app.use(express.json());

  app.use("/api/auth", authRouter);

  app.listen(PORT);
  console.log(`Server is running on: http://localhost:${PORT}`);
};

main();

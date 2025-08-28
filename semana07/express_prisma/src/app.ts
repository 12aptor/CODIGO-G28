import express from "express";
import { userRouter } from "./routes/user.router";
import { authRouter } from "./routes/auth.router";
import { authMiddleware } from "./config/middleware";
import { postRouter } from "./routes/post.router";

const main = () => {
  const app = express();
  const PORT = +process.env.PORT! || 3000;

  app.use(express.json());

  app.get("/", (req, res) => {
    res.send("Bienvenidos a mi API 🤠😎");
  });
  app.use("/api/users", authMiddleware, userRouter);
  app.use("/api/auth", authRouter);
  app.use("/api/posts", authMiddleware, postRouter);

  app.listen(PORT);
  console.log(`Server is running on: http://localhost:${PORT}`);
};

main();

import express from "express";
import { userRouter } from "./routes/user.router";

const main = () => {
  const app = express();
  const PORT = +process.env.PORT! || 3000;

  app.get("/", (req, res) => {
    res.send("Bienvenidos a mi API 🤠😎");
  });
  app.use("/api/user", userRouter);

  app.listen(PORT);
  console.log(`Server is running on: http://localhost:${PORT}`);
};

main();

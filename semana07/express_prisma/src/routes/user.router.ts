import { Router } from "express";
import * as userResource from "../resources/user.resource";

export const userRouter = Router();

userRouter.get("/", userResource.listUsers);
userRouter.post("/", userResource.createUser);
userRouter.put("/:userId", userResource.updateUser);
userRouter.delete("/:userId", userResource.deleteUser);
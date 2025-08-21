import { Router } from "express";
import * as userResource from "../resources/user.resource";

export const userRouter = Router();

userRouter.get("/", userResource.listUsers);

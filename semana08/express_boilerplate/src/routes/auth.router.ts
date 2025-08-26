import { Router } from "express";
import * as authResource from "../resources/auth.resource";

export const authRouter = Router();

authRouter.post("/register", authResource.register);
authRouter.post("/login", authResource.login);

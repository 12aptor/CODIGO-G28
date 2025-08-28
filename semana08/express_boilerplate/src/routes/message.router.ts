import { Router } from "express";
import * as messageResource from "../resources/message.resource";

export const messageRouter = Router();

messageRouter.post("/", messageResource.createMessage);
messageRouter.get("/:channelId", messageResource.getMessages);
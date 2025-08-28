import { Router } from "express";
import * as channelResource from "../resources/channel.resource";

export const channelRouter = Router();

channelRouter.get("/", channelResource.getChannels);
channelRouter.post("/", channelResource.createChannel);

import { Router } from "express";
import * as postResource from "../resources/post.resource";

export const postRouter = Router();

postRouter.get("/", postResource.listPosts);
postRouter.post("/", postResource.createPost);

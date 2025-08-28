import type { Request, Response } from "express";
import { prisma } from "../config/prisma";
import { postSchema } from "../schemas/post.schema";

export const listPosts = async (req: Request, res: Response) => {
  try {
    const posts = await prisma.post.findMany({
      select: {
        id: true,
        title: true,
        content: true,
        published: true,
        created_at: true,
        author: {
          select: {
            id: true,
            name: true,
            email: true,
          },
        },
      },
    });

    res.status(200).json({
      ok: true,
      object: "list_posts",
      data: posts,
    });
  } catch (error) {
    if (error instanceof Error) {
      res.status(400).json({
        ok: false,
        object: "list_posts",
        error: error.message,
      });
    }
  }
};

export const createPost = async (req: Request, res: Response) => {
  try {
    const userId = +req.userId!;

    const { success, data, error } = await postSchema.safeParseAsync(req.body);

    if (!success) {
      res.status(400).json({
        ok: false,
        object: "create_post",
        error: error.issues,
      });
      return;
    }

    const post = await prisma.post.create({
      data: {
        title: data.title,
        content: data.content,
        published: true,
        author_id: userId,
      },
      select: {
        id: true,
        title: true,
        content: true,
        published: true,
        created_at: true,
        author: {
          select: {
            id: true,
            name: true,
            email: true,
          },
        },
      },
    });

    res.status(200).json({
      ok: true,
      object: "create_post",
      data: post,
    });
  } catch (error) {
    if (error instanceof Error) {
      res.status(400).json({
        ok: false,
        object: "create_post",
        error: error.message,
      });
    }
  }
};

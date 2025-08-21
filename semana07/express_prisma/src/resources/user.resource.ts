import type { Request, Response } from "express";
import { prisma } from "../config/prisma";

export const listUsers = async (req: Request, res: Response) => {
  try {
    const users = await prisma.user.findMany();

    res.status(200).json({
      ok: true,
      object: "create_user",
      data: users,
    });
  } catch (error) {
    if (error instanceof Error) {
      res.status(400).json({
        ok: false,
        object: "create_user",
        error: error.message,
      });
    }
  }
};

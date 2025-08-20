import type { Request, Response } from "express";

export const createUser = async (req: Request, res: Response) => {
  try {
    res.status(200).json({
      ok: true,
      object: "create_user",
      data: {
        name: "John Doe",
      },
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

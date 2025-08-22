import type { Request, Response } from "express";
import { loginSchema } from "../schemas/login.schema";
import { prisma } from "../config/prisma";
import bcrypt from "bcrypt";
import jwt from "jsonwebtoken";

export const login = async (req: Request, res: Response) => {
  try {
    const { success, data, error } = await loginSchema.safeParseAsync(req.body);

    if (!success) {
      res.status(400).json({
        ok: false,
        object: "login",
        error: error.issues,
      });
      return;
    }

    const user = await prisma.user.findFirst({
      where: {
        email: data.email,
      },
    });

    if (!user) {
      throw new Error("Unauthorized");
    }

    const isPasswordCorrect = await bcrypt.compare(
      data.password,
      user.password
    );

    if (!isPasswordCorrect) {
      throw new Error("Unauthorized");
    }

    const secretKey = process.env.JWT_SECRET;

    if (!secretKey) {
      throw new Error("JWT_SECRET not found");
    }

    const accessToken = jwt.sign(
      {
        id: user.id,
        name: user.name,
        email: user.email,
      },
      secretKey,
      { expiresIn: "7d" }
    );

    res.status(200).json({
      ok: true,
      object: "login",
      data: {
        access_token: accessToken,
        refresh_token: null,
      },
    });
  } catch (error) {
    if (error instanceof Error) {
      res.status(400).json({
        ok: false,
        object: "login",
        error: error.message,
      });
    }
  }
};

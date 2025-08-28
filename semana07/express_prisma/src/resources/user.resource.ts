import type { Request, Response } from "express";
import { prisma } from "../config/prisma";
import { updateUserSchema, userSchema } from "../schemas/user.schema";
import bcrypt from "bcrypt";

export const listUsers = async (req: Request, res: Response) => {
  try {
    const users = await prisma.user.findMany({
      select: {
        id: true,
        name: true,
        email: true,
      },
    });

    res.status(200).json({
      ok: true,
      object: "list_users",
      data: users,
    });
  } catch (error) {
    if (error instanceof Error) {
      res.status(400).json({
        ok: false,
        object: "list_users",
        error: error.message,
      });
    }
  }
};

export const createUser = async (req: Request, res: Response) => {
  try {
    const { success, data, error } = await userSchema.safeParseAsync(req.body);

    if (!success) {
      res.status(400).json({
        ok: false,
        object: "create_user",
        error: error.issues,
      });
      return;
    }

    const user = await prisma.user.create({
      data: {
        ...data,
        password: await bcrypt.hash(data.password, 10),
      },
      select: {
        id: true,
        name: true,
        email: true,
      },
    });

    res.status(200).json({
      ok: true,
      object: "create_user",
      data: user,
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

export const updateUser = async (req: Request, res: Response) => {
  try {
    const userId = req.params.userId;

    const user = await prisma.user.findUnique({
      where: {
        id: +userId,
      },
    });

    if (!user) {
      throw new Error("User not found");
    }

    const { success, data, error } = await updateUserSchema.safeParseAsync(
      req.body
    );

    if (!success) {
      res.status(400).json({
        ok: false,
        object: "update_user",
        error: error.issues,
      });
      return;
    }

    const updateData = { ...data };

    if (data.password && data.confirm_password) {
      if (data.password !== data.confirm_password) {
        throw new Error("Passwords not match");
      }
      updateData.password = await bcrypt.hash(data.password, 10);
    }

    const updatedUser = await prisma.user.update({
      where: {
        id: +userId,
      },
      data: updateData,
      select: {
        id: true,
        name: true,
        email: true,
      },
    });

    res.status(200).json({
      ok: true,
      object: "update_user",
      data: updatedUser,
    });
    return;
  } catch (error) {
    if (error instanceof Error) {
      res.status(400).json({
        ok: false,
        object: "update_user",
        error: error.message,
      });
    }
  }
};

export const deleteUser = async (req: Request, res: Response) => {
  try {
    const userId = req.params.userId;

    const user = await prisma.user.findUnique({
      where: {
        id: +userId,
      },
    });

    if (!user) {
      throw new Error("User not found");
    }

    await prisma.user.delete({
      where: {
        id: +userId,
      },
    });

    res.status(200).json({
      ok: true,
      object: "delete_user",
      data: null,
    });
  } catch (error) {
    if (error instanceof Error) {
      res.status(400).json({
        ok: false,
        object: "delete_user",
        error: error.message,
      });
    }
  }
};

export const getProfile = async (req: Request, res: Response) => {
  try {
    const userId = req.userId;

    const user = await prisma.user.findUnique({
      where: {
        id: +userId!,
      },
      select: {
        id: true,
        name: true,
        email: true,
      }
    });

    if (!user) {
      throw new Error("User not found");
    }

    res.status(200).json({
      ok: true,
      object: "get_user",
      data: user,
    });
  } catch (error) {
    if (error instanceof Error) {
      res.status(400).json({
        ok: false,
        object: "get_user",
        error: error.message,
      });
    }
  }
};

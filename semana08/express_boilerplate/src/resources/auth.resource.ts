import type { Request, Response } from "express";
import { loginSchema, registerSchema } from "../schemas/auth.schema";
import { ZodError } from "zod";
import { connectDB } from "../config/mongodb";
import bcrypt from "bcrypt";
import jwt from "jsonwebtoken";

export const register = async (req: Request, res: Response) => {
  try {
    const data = await registerSchema.parseAsync(req.body);

    const db = await connectDB();
    const collection = db.collection("users");

    const existingUser = await collection.findOne({
      email: data.email,
    });
    if (existingUser) {
      throw new Error("User already exists");
    }

    const user = await collection.insertOne({
      name: data.name,
      email: data.email,
      password: await bcrypt.hash(data.password, 10),
    });

    const createdUser = await collection.findOne(
      { _id: user.insertedId },
      { projection: { password: 0 } }
    );

    res.json({
      ok: true,
      object: "register",
      data: createdUser,
    });
    return;
  } catch (error) {
    if (error instanceof ZodError) {
      res.status(400).json({
        ok: false,
        object: "register",
        error: error.issues,
      });
      return;
    } else if (error instanceof Error) {
      res.status(400).json({
        ok: false,
        object: "register",
        error: error.message,
      });
      return;
    }
  }
};

export const login = async (req: Request, res: Response) => {
  try {
    const data = await loginSchema.parseAsync(req.body);

    const db = await connectDB();
    const collection = db.collection("users");

    const user = await collection.findOne({
      email: data.email,
    });

    if (!user) {
      throw new Error("Unauthorized");
    }

    const validPassword = await bcrypt.compare(data.password, user.password);

    if (!validPassword) {
      throw new Error("Unauthorized");
    }

    const secretKey = process.env.SECRET_KEY;
    if (!secretKey) {
      throw new Error("Missing secret key");
    }

    const accessToken = jwt.sign(
      {
        id: user._id,
        name: user.name,
        email: user.email,
      },
      secretKey,
      { expiresIn: "7d" }
    );

    res.json({
      ok: true,
      object: "login",
      data: {
        access: accessToken,
        refresh: accessToken,
      },
    });
  } catch (error) {
    console.log(error);
    if (error instanceof ZodError) {
      res.status(400).json({
        ok: false,
        object: "login",
        error: error.issues,
      });
      return;
    } else if (error instanceof Error) {
      res.status(400).json({
        ok: false,
        object: "login",
        error: error.message,
      });
      return;
    }
  }
};

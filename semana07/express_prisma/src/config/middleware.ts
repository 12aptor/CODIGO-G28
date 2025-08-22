import type { Request, Response, NextFunction } from "express";
import jwt, { type JwtPayload } from "jsonwebtoken";

declare global {
  namespace Express {
    interface Request {
      userId?: string;
    }
  }
}

interface CustomJwtPayload extends JwtPayload {
  id: number;
  name: string;
  email: string;
}

export const authMiddleware = async (
  req: Request,
  res: Response,
  next: NextFunction
) => {
  try {
    const bearerToken = req.headers.authorization;

    if (!bearerToken) {
      throw new Error("Unauthorized");
    }

    if (!bearerToken.startsWith("Bearer ")) {
      throw new Error("Unauthorized");
    }

    const token = bearerToken.split(" ")[1];

    const secretKey = process.env.JWT_SECRET;

    if (!secretKey) {
      throw new Error("JWT_SECRET not found");
    }

    const decodedToken = jwt.verify(token, secretKey) as CustomJwtPayload;

    if (!decodedToken.id) {
      throw new Error("Unauthorized");
    }

    req.userId = decodedToken.id.toString();

    next();
  } catch (error) {
    if (error instanceof Error) {
      res.status(401).json({
        ok: false,
        object: "auth",
        error: error.message,
      });
    }
  }
};

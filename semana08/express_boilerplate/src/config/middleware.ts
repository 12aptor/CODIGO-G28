import type { Request, Response, NextFunction } from "express";
import jwt, { JwtPayload } from "jsonwebtoken";

declare global {
  namespace Express {
    interface Request {
      userId?: string;
    }
  }
}

interface CustomJwtPayload extends JwtPayload {
  id: string;
  name: string;
  email: string;
}

export const authMiddleware = (
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
    const secretKey = process.env.SECRET_KEY;
    if (!secretKey) {
      throw new Error("Missing secret key");
    }

    const decodedToken = jwt.verify(token, secretKey) as CustomJwtPayload;
    if (!decodedToken.id) {
      throw new Error("unauthorized");
    }

    req.userId = decodedToken.id;

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

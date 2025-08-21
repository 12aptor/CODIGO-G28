import { z } from "zod";

export const userSchema = z.object({
  name: z.string(),
  email: z.email(),
  password: z.string(),
});

export const updateUserSchema = z.object({
  name: z.string(),
  email: z.email(),
  password: z.string().optional(),
  confirm_password: z.string().optional(),
});

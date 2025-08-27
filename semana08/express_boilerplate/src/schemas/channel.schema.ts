import { z } from "zod";

export const channelSchema = z.object({
  name: z.string(),
  type: z.enum(["TEXT", "VOICE"]),
});

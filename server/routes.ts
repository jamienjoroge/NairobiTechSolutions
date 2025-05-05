import type { Express } from "express";
import { createServer, type Server } from "http";
import { storage } from "./storage";
import { contactSchema } from "@shared/schema";
import { z } from "zod";

export async function registerRoutes(app: Express): Promise<Server> {
  // Contact form submission
  app.post("/api/contact", async (req, res) => {
    try {
      // Validate request body
      const contactData = contactSchema.parse(req.body);
      
      // Store the contact data
      const contact = await storage.saveContactRequest(contactData);
      
      // In a real application, we would send an email here
      // For now, we'll just return the contact data
      
      res.status(200).json({ 
        message: "Contact request saved successfully", 
        contactId: contact.id 
      });
    } catch (error) {
      if (error instanceof z.ZodError) {
        res.status(400).json({ message: "Invalid form data", errors: error.errors });
      } else {
        console.error("Error saving contact request:", error);
        res.status(500).json({ message: "Failed to save contact request" });
      }
    }
  });

  const httpServer = createServer(app);
  return httpServer;
}

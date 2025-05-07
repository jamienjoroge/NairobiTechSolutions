import { contacts, type Contact, type InsertContact } from "@shared/schema";
import { db } from "./db";
import { eq } from "drizzle-orm";

// modify the interface with any CRUD methods
// you might need

export interface IStorage {
  saveContactRequest(contact: InsertContact): Promise<Contact>;
}

// Database implementation using Drizzle ORM
export class DatabaseStorage implements IStorage {
  async saveContactRequest(contactData: InsertContact): Promise<Contact> {
    const [contact] = await db
      .insert(contacts)
      .values(contactData)
      .returning();
    console.log(`Contact request received from ${contactData.name} (${contactData.email})`);
    return contact;
  }
}

// Memory implementation (keeping for reference)
export class MemStorage implements IStorage {
  private contacts: Map<number, Contact>;
  currentContactId: number;

  constructor() {
    this.contacts = new Map();
    this.currentContactId = 1;
  }
  
  async saveContactRequest(contactData: InsertContact): Promise<Contact> {
    const id = this.currentContactId++;
    const now = new Date();
    const contact: Contact = { 
      ...contactData,
      id,
      createdAt: now.toISOString()
    };
    this.contacts.set(id, contact);
    console.log(`Contact request received from ${contactData.name} (${contactData.email})`);
    return contact;
  }
}

// Switch to database storage
export const storage = new DatabaseStorage();

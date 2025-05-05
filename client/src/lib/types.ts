import { ReactNode } from 'react';

export interface ServiceCard {
  icon: ReactNode;
  title: string;
  description: string;
}

export interface TeamMember {
  name: string;
  position: string;
  bio: string;
  image: string;
}

export interface ContactInfo {
  icon: ReactNode;
  title: string;
  value: string;
  link?: string;
}

export interface ContactFormData {
  name: string;
  email: string;
  service: string;
  message: string;
}

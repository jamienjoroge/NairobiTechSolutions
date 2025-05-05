# SaharaNova - Nairobi Tech Consultancy

A modern, SEO-optimized single-page website for SaharaNova, a Nairobi-based technology consultancy specializing in digital transformation, software solutions, and IT services.

## Features

- **Responsive Design**: Fully mobile-responsive layout that looks great on all devices
- **Modern UI**: Built with React and Tailwind CSS for a sleek, contemporary appearance
- **Component-Based Architecture**: Modular design for easy maintenance and updates
- **Contact Form**: Client inquiry submission with server-side validation and database storage
- **PostgreSQL Integration**: Persistent storage of contact submissions

## Tech Stack

- **Frontend**: React, Tailwind CSS, Shadcn UI components
- **Backend**: Node.js, Express
- **Database**: PostgreSQL
- **ORM**: Drizzle ORM with Zod validation
- **State Management**: React Query

## How to Run

1. Clone the repository
2. Install dependencies: `npm install`
3. Set up environment variables:
   - Copy `.env.example` to `.env` and update the values as needed.
4. Set up PostgreSQL database and update connection details in `.env`
5. Run database migrations: `npm run db:push`
6. Start the application:
   - For development, run the backend: `npm run dev`
   - If the frontend is served separately, run it with: `npm run client:dev` (add this script if needed)
7. For production, build and start: `npm run build && npm start`

## Project Structure

- `/client`: Frontend React application
- `/server`: Backend Express server
- `/shared`: Shared code and database schema
- `/client/src/components`: UI components
- `/client/src/pages`: Page components

## Screenshots

(Add screenshots here)

## License

Copyright © 2025 SaharaNova Tech Consultancy
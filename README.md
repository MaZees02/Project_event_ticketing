<<<<<<< HEAD

=======
🎟️ Event Ticketing System

A modular event ticketing platform built with FastAPI.
It allows users to register, browse events, purchase tickets via Paystack, and receive QR-code-based tickets via email.

📌 Features

User Service – User registration, authentication (JWT), and profile management.

Event Service – CRUD for events, public listing & filtering.

Payment Service – Integration with Paystack (with circuit breaker fallback).

Ticket Service – Ticket issuance, QR code generation, email delivery.

Dockerized for easy deployment.

🏗️ Architecture

Project_event_ticketing/
├─ event_ticketing_system/
│  ├─ main.py
│  ├─ db.py
│  ├─ crud.py
│  ├─ models.py
│  ├─ schemas.py
│  ├─ routers/
│  └─ .env
├─ Dockerfile
├─ docker-compose.yml
├─ requirements.txt
├─ README.md
└─ .gitignore



Services will be available at:
# Merged Event Ticketing System

This repository merges the four microservices (`event_service`, `payment_service`, `user_service`, `ticket_service`) into a single FastAPI application with router-based modules for each service. This structure makes it easy to deploy a single container (for example to Render).

## Quick start (SQLite, local)
1. Create a virtualenv and install:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # or .venv\Scripts\activate on Windows
   pip install -r requirements.txt



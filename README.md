FastAPI City Temperature Management API

Overview

This project is a FastAPI-based application for managing cities and their temperatures. It provides CRUD operations for cities and temperatures, integrates with an external weather API to fetch real-time temperature data, and stores results in a relational database.

Features

Create, list, and delete cities

Create and list temperatures for cities

Update temperatures by fetching data from an online weather API

Asynchronous HTTP requests with parallel execution for performance

Database models: City and Temperature

Requirements

Python 3.11+

FastAPI

SQLAlchemy

Pydantic

httpx

Uvicorn

Setup Instructions

Clone the repository:

git clone <repository-url>
cd py-fastapi-city-temperature-management-api

Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

Install dependencies:

pip install -r requirements.txt

Run database migrations (if applicable).

Start the application:

uvicorn app.main:app --reload

API Endpoints

POST /cities — Create a new city

GET /cities — List all cities

DELETE /cities/{city_id} — Delete a city

POST /temperatures/update — Fetch and store updated temperatures from weather API

GET /temperatures — List temperatures (optionally filter by city_id)

Design Choices

Table Names: City and Temperature to match requirements.

Async Integration: Uses httpx.AsyncClient with asyncio.gather for concurrent API calls.

Schemas: Pydantic models ensure validation and serialization.

Repository Hygiene: .gitignore excludes local database files (e.g., cities.db).

Assumptions

Weather API endpoint (wttr.in) is used for simplicity and does not require an API key.

Database is SQLite for local development; can be swapped for PostgreSQL/MySQL in production.

Running Tests

To run unit tests:

pytest

Future Improvements

Add authentication and user management

Implement update endpoints for cities

Enhance error handling for external API failures

Add Docker support for containerized deployment

# Stock Insights Assistant

A small web application that lets users ask natural language questions about stocks and receive AI-powered answers backed by live market data.

The goal of this project was to build a minimal but well-structured system that demonstrates natural language query handling, external data integration, and a clean architecture that is easy to extend and test.

---

## Features

- Ask questions about stocks in natural language
- Query interpretation using OpenAI
- Live stock data retrieval
- Clear, human-readable responses
- Simple web interface
- Dockerized setup
- CI pipeline running linting and tests

---

## Example Query

Input:

```
How is MSFT doing today?
```

Example output:

```
Microsoft Corporation (MSFT) is trading at 408.96 USD today, down 1.72 (0.42%).
```

---

## Architecture Overview

The application is split into a few simple layers:

- **API / UI layer** – handles HTTP requests and serves the web interface  
- **AI layer** – interprets natural language queries using OpenAI  
- **Routing / business logic** – determines how to handle the parsed query  
- **Data access layer** – retrieves stock data from external APIs  
- **Response generation** – formats the final answer returned to the user  

This separation keeps the core logic easy to test and extend.

---

## Running the Application

From the project root:

```bash
docker compose up --build
```

Once the container starts, open:

```
http://localhost:8000
```

---

### Running locally (Testing)

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the server:

```bash
uvicorn app.main:app --reload
```

Open:

```
http://localhost:8000
```

---

## Environment Variables

Create a `.env` file using the example provided.

```
OPENAI_API_KEY=your_openai_api_key_here
```

---

## Running Tests

```bash
pytest
```

---

## Linting

```bash
ruff check .
```

---

## CI

GitHub Actions runs linting and tests on every push to ensure the codebase stays valid.

---

## Interesting Future Improvements

- Allow for more quirky user queries
- Add caching for repeated queries improving memory
- Improve frontend UX design - make more user friendly
- More unit tests
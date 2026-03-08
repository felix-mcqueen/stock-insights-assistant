# Stock Query App

This project parses natural language stock questions, identifies the ticker symbol, fetches live market data, and returns a human-readable response.

## Features
- Natural language query parsing
- Intent classificationa# Stock Insights Assistant

A small web application that lets users ask natural language questions about stocks and receive AI-powered answers backed by live market data.

This project was built as a take-home task for a Data Engineer role. It focuses on clean separation of concerns, simple extensible architecture, testability, and reliable local execution through Docker Compose.

## Features

- Ask natural language questions about stocks
- Interpret user intent using the OpenAI API
- Fetch live stock market data from Yahoo Finance endpoints
- Return concise, human-readable answers
- Simple web UI
- Dockerized for consistent local execution
- GitHub Actions CI for linting and tests
- Unit tests for core business logic

## Example Questions

- `How is AAPL doing today?`
- `How is Microsoft doing today?`
- `Compare TSLA and F`
- `What is NVDA doing today?`

## Architecture Overview

The application is split into a few small components:

- **API/UI layer**: serves the web page and handles form submissions
- **AI layer**: uses OpenAI to interpret the user’s natural language query into structured intent
- **Business logic/router**: decides how to handle the parsed query
- **Data fetching layer**: retrieves stock data from an external market data endpoint
- **Response generation layer**: formats stock data into a readable answer
- **Tests**: validate core parsing and routing behavior without depending on live external APIs where possible

A typical request flow is:

1. User enters a stock question in the web UI
2. The app sends the question to OpenAI for interpretation
3. The parsed result is routed to the appropriate handler
4. The handler fetches relevant stock data
5. The app formats and displays the final answer in the UI

## Tech Stack

- Python 3.11
- FastAPI
- Jinja2
- OpenAI Python SDK
- Requests
- Docker / Docker Compose
- Pytest
- Ruff
- GitHub Actions

## Project Structure

```text
.
├── app/
│   ├── main.py
│   ├── api.py
│   ├── ai_client.py
│   ├── parser.py
│   ├── router.py
│   ├── data_fetcher.py
│   ├── response_generator.py
│   ├── models.py
│   └── templates/
│       └── index.html
├── tests/
│   ├── test_parser.py
│   └── test_router.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md
- Ticker extraction
- Live stock data retrieval from Yahoo Finance
- Formatted response output

## Installation

```bash
pip install -r requirements.txt
# 🤖 AI Customer Ticket Bot

> An intelligent customer support system powered by RAG (Retrieval-Augmented Generation) that uses AI and Natural Language Processing to manage, categorize, and respond to customer service tickets efficiently.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Environment Variables](#environment-variables)
- [Usage](#usage)
  - [Run via FastAPI](#run-via-fastapi)
  - [Run Standalone Script](#run-standalone-script)
- [API Reference](#api-reference)
- [Deployment](#deployment)
- [Contributing](#contributing)

---

## 🧠 Overview

The **AI Customer Ticket Bot** is a production-ready RAG pipeline that ingests customer support ticket data, embeds it into a persistent vector store, and answers natural language queries using a powerful LLM. It exposes a clean REST API via FastAPI, making it easy to integrate into any support workflow.

**Key capabilities:**
- 📥 Ingests CSV-based customer support ticket data with rich metadata
- 🔍 Performs semantic similarity search using Chroma vector store
- 🧩 Chunks documents intelligently with overlapping windows for better context retrieval
- 💬 Answers questions about tickets using a hosted LLM via OpenRouter
- 🚀 Deployable to any platform that supports a `Procfile` (e.g., Heroku, Railway)

---

## 🏗️ Architecture

```
CSV Data
   │
   ▼
Data Ingestion (Data_injestion.py)
   │  Converts rows → LangChain Documents with metadata
   ▼
Chunking (chunking_overlaping.py)
   │  RecursiveCharacterTextSplitter (chunk=400, overlap=80)
   ▼
Embedding & Vector Store (embeding_vectorstore.py)
   │  Qwen Embedding Model via OpenRouter → ChromaDB (persistent)
   ▼
Retrieval QA Chain (Retrieval_metadata.py)
   │  similarity search (k=3) → RetrievalQA with LLM
   ▼
FastAPI Endpoint (app.py)
   │  POST /ask → { "answer": "..." }
   ▼
Client / Integration
```

---

## 📁 Project Structure

```
AI-customer_Ticket_bot/
│
├── Data/                          # Raw & cleaned CSV ticket data
│   └── customer_support_ticket_cleaned.csv
│
├── Model/                         # Persisted ChromaDB vector store
│
├── app.py                         # FastAPI application entry point
├── main_excution.py               # Standalone script for local testing
│
├── Data_injestion.py              # CSV loader → LangChain Documents
├── chunking_overlaping.py         # Document chunking with overlap
├── embeding_vectorstore.py        # Embedding model + ChromaDB setup
├── Retrieval_metadata.py          # RAG chain construction
├── llm_setup.py                   # LLM configuration (OpenRouter)
├── load_env.py                    # Environment variable loader
├── config.py                      # Logging configuration
│
├── Procfile.txt                   # Deployment process definition
├── requirements.txt               # Python dependencies
└── README.md
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **API Framework** | FastAPI + Uvicorn |
| **LLM** | OpenRouter (`openai/gpt-oss-120b:free`) |
| **Embeddings** | OpenRouter (`qwen/qwen3-embedding-8b`) |
| **Vector Store** | ChromaDB (persistent, local) |
| **RAG Framework** | LangChain |
| **Data Processing** | Pandas |
| **Config / Secrets** | python-dotenv |
| **Logging** | Python `logging` module |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- An [OpenRouter](https://openrouter.ai/) account with API keys
- Git

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Musawir456/AI-customer_Ticket_bot.git
cd AI-customer_Ticket_bot

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the root directory:

```env
# Used by the LLM (llm_setup.py)
OPENROUTER_API_KEY_1=your_openrouter_api_key_for_llm

# Used by the embedding model (embeding_vectorstore.py)
OPENROUTER_API_KEY=your_openrouter_api_key_for_embeddings

# OpenRouter base URL
OPENROUTER_API_BASE=https://openrouter.ai/api/v1
```

> ⚠️ **Never commit your `.env` file.** Add it to `.gitignore`.

---

## 💻 Usage

### Run via FastAPI

```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`. Visit `http://localhost:8000/docs` for the interactive Swagger UI.

### Run Standalone Script

For local testing without the API server:

```bash
python main_excution.py
```

This loads the data, builds the vector store, and runs a sample query directly in the terminal.

---

## 📡 API Reference

### `POST /ask`

Submit a natural language question about your customer support tickets.

**Request Body:**

```json
{
  "question": "Why are customers unhappy with high priority tickets?"
}
```

**Response:**

```json
{
  "answer": "Based on the retrieved tickets, customers with high priority issues are dissatisfied due to..."
}
```

**Example with `curl`:**

```bash
curl -X POST "http://localhost:8000/ask" \
     -H "Content-Type: application/json" \
     -d '{"question": "What are the most common billing issues?"}'
```

---

## ☁️ Deployment

This project is configured for deployment on platforms that support `Procfile`-based deployments (Heroku, Railway, Render, etc.).

The `Procfile` contains:

```
web: uvicorn app:app --host 0.0.0.0 --port $PORT
```

**Steps:**
1. Push your code to GitHub
2. Connect your GitHub repo to your hosting platform
3. Set the environment variables in your platform's dashboard
4. Deploy — the `Procfile` will handle the rest

> 💡 **Note:** The ChromaDB vector store is persisted locally. For cloud deployments, consider using a managed vector database or mounting a persistent volume.

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes and commit: `git commit -m "Add your feature"`
4. Push to your fork: `git push origin feature/your-feature-name`
5. Open a Pull Request


---

<div align="center">
  Built with ❤️ by <a href="https://github.com/Musawir456">Musawir456</a>
</div>

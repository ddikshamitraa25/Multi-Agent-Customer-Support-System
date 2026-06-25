# Multi-Agent Customer Support Automation System

## Overview

A multi-agent AI-powered customer support platform that automates customer query handling through intelligent routing, retrieval-augmented generation (RAG), conversation memory, and human approval workflows.

The system classifies customer queries, routes them to specialized support agents, retrieves relevant information from organizational knowledge bases, stores conversation history using SQLite, and generates professional responses using Large Language Models.

---

## Features

### 1. Intent Classification
Classifies customer queries into one of the following categories:
- Sales
- Technical
- Billing
- Account

### 2. Department Routing
Automatically routes the query to the appropriate department agent.

### 3. Specialized Agents
Dedicated agents handle:
- Sales queries
- Technical support queries
- Billing queries
- Account-related queries

### 4. Retrieval-Augmented Generation (RAG)
Retrieves relevant information from company documents using vector embeddings and ChromaDB.

### 5. SQLite Memory
Stores customer interactions and retrieves previous conversations when required.

### 6. Human-in-the-Loop
Sensitive requests such as refund requests require manual approval.

### 7. Supervisor Agent
Reviews responses and generates professional final responses for customers.

---

## Technologies Used

- Python 3.12
- LangGraph
- LangChain
- Groq API (Llama 3.3 70B Versatile)
- ChromaDB
- SQLite
- Sentence Transformers
- FAISS
- Python Dotenv

---

## Project Architecture

Customer Query
↓
Intent Classification
↓
Department Routing
↓
Specialized Agent
↓
RAG Retrieval
↓
SQLite Memory
↓
Human Approval (if required)
↓
Supervisor Agent
↓
Final Response

---

## Project Structure

```text
VIT-IBM-Agentic-AI-Assignment-2/
│
├── app.py
├── graph.py
├── agents.py
├── rag.py
├── memory.py
├── approval.py
├── supervisor.py
├── state.py
│
├── requirements.txt
├── README.md
├── memory.db
├── workflow.png
├── Screenshots.pdf
├── .env
│
├── documents/
│   ├── faq.txt
│   ├── technical_manual.txt
│   ├── pricing_guide.txt
│   └── company_policy.txt
│
└── chroma_db/
```

---

## Installation Steps

### Step 1: Create Virtual Environment

```bash
python -m venv venv
```

### Step 2: Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variable

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

### Step 5: Run the Project

```bash
python app.py
```

---

## Sample Queries

### Account Query

```text
How can I reset my password?
```

### Billing Query

```text
I want a refund.
```

### Technical Query

```text
My application crashes.
```

### Sales Query

```text
What are your pricing plans?
```

### Memory Recall Query

```text
What was my previous issue?
```

---

## Outputs Demonstrated

- Intent Classification
- Department Routing
- RAG Retrieval
- SQLite Memory Storage and Recall
- Human-in-the-Loop Approval
- Supervisor Response Generation

---

## Author

## Author

Diksha

B.Tech Computer Science Student | AI & Software Development Enthusiast

🚀 AI Project Manager — Autonomous Multi-Agent Orchestration Framework

An autonomous multi-agent AI system built using LangGraph that dynamically decomposes complex user goals into structured execution graphs, coordinating multiple specialized agents through adaptive workflows, cyclic feedback loops, and persistent conversational memory.

📌 Overview

This project implements an intelligent AI orchestration engine composed of multiple specialized agents working together to analyze tasks, perform research, design solutions, optimize results, and generate high-quality final outputs.

Unlike traditional single-prompt systems, this framework leverages graph-based execution pipelines to enable:

Task decomposition

Iterative reasoning

Agent collaboration

Cyclic refinement

Stateful memory management

This architecture enables scalable, extensible, and production-ready multi-agent AI workflows.

🧠 System Architecture

The system consists of four specialized agents, coordinated through a LangGraph StateGraph execution pipeline:

🔹 Performer Agent

Understands the original user task

Defines requirements and output format

Synthesizes all agent outputs into a structured final response

🔹 Research Agent

Collects relevant technical insights

Gathers best practices and architectural ideas

Produces concise research summaries

🔹 Developer Agent

Designs solution architectures

Proposes implementation strategies

Generates Python code snippets and system designs

🔹 Analyst Agent

Optimizes performance, scalability, and security

Evaluates cost-efficiency

Provides system improvements and refinements

🔁 Execution Flow

The system operates as a cyclic execution graph, enabling iterative refinement:

START → Performer → Research → Developer → Analyst → Performer → END


This cyclic design allows the system to continuously refine outputs, ensuring higher quality results compared to linear pipelines.

🧩 Core Features

🧠 Multi-Agent Reasoning – Specialized agents collaborate through structured workflows

🔁 Cyclic Feedback Loops – Continuous refinement until optimal results are achieved

🗂 Centralized Memory Management – Persistent state using LangGraph checkpointing

🏗 Graph-Based Execution Engine – Adaptive task routing using LangGraph StateGraph

🔧 Modular Agent Design – Easily extensible to support new tools or agents

🛠️ Tech Stack

Python 3.11+

LangGraph

LangChain

Ollama (LLaMA 3.2)

PostgreSQL (Optional - for persistent checkpointing)

📂 Project Structure
AI-project-manager/
│
├── main.py              # Main orchestration pipeline
├── agents/              # Agent logic (optional modularization)
├── memory/              # Memory and checkpointing utilities
├── requirements.txt     # Dependencies
└── README.md

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/zeinabkobaissi/AI-project-manager.git
cd AI-project-manager

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Install & Run Ollama

Download and install Ollama:

👉 https://ollama.com

Pull the model:

ollama pull llama3.2

▶️ Running the System
python main.py


You will be prompted to enter a task:

Enter your task: Build a scalable microservices backend architecture


The system will automatically:

Analyze the task

Research best practices

Design architecture

Optimize performance

Produce a final professional solution

🧠 Memory Management

This system uses LangGraph checkpointing for state persistence:

Default: InMemorySaver (for fast local testing)

Optional: PostgresSaver (for persistent long-term memory)

Enable PostgreSQL Memory (Optional)
from langgraph.checkpoint.postgres import PostgresSaver
checkpointer = PostgresSaver.from_conn_string("postgresql://user:pass@localhost:5432/dbname")


This enables multi-session conversational memory and workflow recovery.


🏆 Why This Project Matters

This system demonstrates:

Advanced LLM orchestration architecture

Production-grade multi-agent workflows

Strong understanding of AI system design patterns

Real-world agent collaboration engineering

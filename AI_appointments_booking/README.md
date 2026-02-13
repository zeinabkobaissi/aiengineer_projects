AI Appointment Booking Agent
Production-Style MCP + Local LLM Tool-Calling System

A production-oriented AI agent that uses a local Large Language Model (LLM) with Model Context Protocol (MCP) to securely create, list, and delete appointments via natural language.

This project demonstrates real-world AI system architecture, including tool-calling, client–server separation, controlled execution, and persistent storage — similar to modern AI agent systems used in production.

Key Highlights (Recruiter Focus)

Production-style AI agent architecture

Secure tool invocation via MCP protocol

Local LLM integration using Ollama (llama3.2)

Structured tool schemas with controlled execution

Persistent storage layer using CSV

Async client–server communication

Real tool-calling (not simulated)

Fully local — no external APIs required

System Architecture
                ┌─────────────────────┐
                │        User         │
                └──────────┬──────────┘
                           │ Natural Language
                           ▼
                ┌─────────────────────┐
                │     MCP Client      │
                │  (Agent Controller) │
                └──────────┬──────────┘
                           │ Tool schemas
                           ▼
                ┌─────────────────────┐
                │     Ollama LLM      │
                │     (llama3.2)      │
                └──────────┬──────────┘
                           │ Tool call decision
                           ▼
                ┌─────────────────────┐
                │     MCP Server      │
                │   (Tool Provider)   │
                └──────────┬──────────┘
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
create_appointment   list_appointments   delete_appointment
        │                  │                  │
        └──────────────┬───┴───────────────┘
                       ▼
               appointments.csv
                (Persistence)

Why This Project Matters

Modern AI systems do NOT allow LLMs direct access to databases or systems.

Instead, they use controlled tool access.

This project replicates that exact architecture using MCP.

This is the same architectural pattern used in:

OpenAI tool-calling agents

LangGraph agent systems

Production AI assistants

Autonomous AI workflows

Core Components
MCP Server

Defines secure tools:

create_appointment
list_appointments
delete_appointment


The server exposes tools with structured schemas.

The LLM cannot access files directly.

MCP Client (Agent Controller)

Responsible for:

Connecting to MCP server

Sending tool schemas to LLM

Handling tool calls

Executing tools safely

Returning results to LLM

LLM Layer (Ollama)

Model used:

llama3.2


Responsible for:

Understanding user intent

Selecting correct tool

Generating tool arguments

Storage Layer

CSV persistence:

appointments.csv


Example:

name,date,time
Zeinab,Monday,4:00 to 5:00
Mariam,Friday,8:00 to 9:00

Example Execution Flow

User input:

Book an appointment for Zeinab on Monday at 4:00 to 5:00


Execution pipeline:

User → MCP Client → LLM
LLM → Tool Call Decision
Tool → MCP Server
Server → CSV Storage
Result → LLM → User

Example Tool Call (Internal)
{
  "name": "create_appointment",
  "arguments": {
    "name": "Zeinab",
    "date": "Monday",
    "time": "4:00 to 5:00"
  }
}

Technologies Used

Core AI stack:

Python

Model Context Protocol (MCP)

Ollama (Local LLM runtime)

llama3.2 model

System stack:

AsyncIO

JSON-RPC

CSV persistence

Structured tool schemas

Architecture patterns:

Agent architecture

Tool-calling pattern

Client–server architecture

Controlled execution model

Installation
Install Ollama

https://ollama.com

Pull model:

ollama pull llama3.2

Install dependencies
pip install mcp ollama asyncio

Running the System

Start MCP server:

python mcp_server.py


Start MCP client:

python mcp_client.py

Example Usage

Create appointment:

Book an appointment for Mariam on Friday at 8:00 to 9:00


List appointments:

List appointments


Delete appointment:

Delete appointment for Zeinab on Monday at 4:00 to 5:00

Engineering Challenges Solved

Tool-calling integration with local LLM

Secure tool execution via MCP

Client-server async communication

Schema mapping between MCP and Ollama

Persistent storage integration

Tool execution lifecycle management

Skills Demonstrated (AI Engineering Focus)

LLM Tool-Calling Architecture

AI Agent System Design

MCP Protocol Integration

Local LLM Deployment

Structured Tool Schema Design

Async Python Systems

AI System Architecture

Agent Control Flow Design

Persistent Storage Integration

Production Concepts Demonstrated

This project demonstrates core production AI engineering concepts:

Tool abstraction layer

Controlled LLM execution

Separation of concerns

Agent orchestration

Persistent storage integration

Local AI deployment

Future Improvements

Database integration (PostgreSQL)

Conflict detection

LangGraph orchestration

REST API interface

Web frontend

Authentication

Multi-user support

Vector database integration

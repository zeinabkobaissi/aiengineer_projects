AI Appointment Booking Agent (MCP + Local LLM)

An AI-powered appointment scheduling agent built using the Model Context Protocol (MCP) and a local Large Language Model (LLM) via Ollama.
The system allows users to create, list, and delete appointments using natural language while ensuring secure, structured tool execution.

This project demonstrates a production-style AI agent architecture with proper client–server separation, tool schemas, and persistent storage.

Features

• Natural language appointment booking
• Secure tool execution using MCP protocol
• Local LLM integration using Ollama (llama3.2)
• Create, list, and delete appointments
• Persistent storage using CSV
• Client–server architecture
• Async tool execution
• Fully local (no external APIs required)

System Architecture

User Input
↓
MCP Client (Agent Controller)
↓
Local LLM (Ollama llama3.2)
↓
MCP Server (Tool Provider)
↓
Tool Execution
↓
CSV Storage (appointments.csv)
↓
Response returned to user

Architecture Components
1. MCP Client

Responsible for:

• Connecting to MCP server
• Sending tool schemas to LLM
• Handling tool calls
• Executing tools securely
• Returning results to LLM

2. MCP Server

Provides structured tools:

• create_appointment
• list_appointments
• delete_appointment

The server exposes tools with defined schemas.
The LLM cannot access files directly.

3. LLM Layer (Ollama)

Model used:

llama3.2

Responsible for:

• Understanding user intent
• Selecting appropriate tool
• Generating tool arguments

4. Storage Layer

File used:

appointments.csv

Example:

name,date,time
Zeinab,Monday,4:00 to 5:00
Mariam,Friday,8:00 to 9:00

Project Structure
project/
│
├── mcp_server.py
├── mcp_client.py
├── appointments.csv
├── README.md

Example Usage

Create appointment:

Book an appointment for Zeinab on Monday from 4:00 to 5:00

List appointments:

List all appointments

Delete appointment:

Delete appointment for Zeinab on Monday from 4:00 to 5:00

Example Tool Call (Internal)
create_appointment(
  name="Zeinab",
  date="Monday",
  time="4:00 to 5:00"
)

Technologies Used

AI and Agent Stack:

• Python
• Model Context Protocol (MCP)
• Ollama
• llama3.2

System and Backend:

• AsyncIO
• JSON-RPC
• CSV storage

Architecture Patterns:

• AI agent architecture
• Tool-calling pattern
• Client–server architecture
• Controlled execution model

Installation

Install Ollama:

https://ollama.com

Pull model:

ollama pull llama3.2


Install dependencies:

pip install mcp ollama asyncio

Running the System

Start MCP server:

python mcp_server.py


Start MCP client:

python mcp_client.py

Example Execution Flow

User:

Book appointment for Mariam on Friday from 8:00 to 9:00

System flow:

User → Client → LLM → Tool Call → MCP Server → CSV → Response

Engineering Concepts Demonstrated

• AI agent orchestration
• Tool-calling architecture
• Local LLM deployment
• Client–server AI systems
• Structured tool schema design
• Persistent storage integration
• Async system design

Production Concepts Demonstrated

• Controlled LLM execution
• Tool abstraction layer
• Secure tool invocation
• Separation of concerns
• Agent control flow

Future Improvements

• Database integration (PostgreSQL)
• Conflict detection
• Web interface
• REST API
• Multi-user support
• Authentication
• Vector database integration

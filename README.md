

![Uploading Screenshot 2025-06-18 204815.png…]()



# llama3-ai-web-summarizer
A Python-based AI summarization tool powered by Groq's LLaMA 3-70B model using pydantic_ai and MCPServerStdio. This script fetches and summarizes the content of a given webpage, demonstrating how to build an AI agent that integrates with MCP (Multi-Component Protocol) for enhanced modularity and flexibility.

# 🧠 llama3-ai-web-summarizer

A powerful and lightweight AI web summarizer that leverages Groq's LLaMA 3-70B model via `pydantic_ai` and MCP protocol.

## 🚀 Features
- Utilizes `pydantic_ai.Agent` for structured, LLM-based tasks.
- Uses MCP server as a modular fetcher for external content.
- Summarizes the content of a given webpage.
- Async architecture for efficient performance.

## 🛠️ Tech Stack
- Python
- pydantic_ai
- Groq API (LLaMA 3-70B)
- MCPServerStdio

## 🧪 Example Use
```bash
python main.py

This will:

-etch the contents of the provided Wikipedia page

Run the summarization using the LLaMA 3 model

Output the summary in the terminal

🗝️ Setup
Set your GROQ_API_KEY in the environment or update it in the script.

Ensure mcp_server_fetch is available as a module.

Install necessary packages:

bash
Copy code
pip install pydantic_ai

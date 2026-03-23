**AI Agentic Researcher 🔍🤖**

A sophisticated AI Agent capable of autonomous web research and data synthesis. Built using LangGraph for stateful orchestration and Llama 3.1 (via Ollama) as the reasoning engine, this project demonstrates how to bridge the gap between static LLMs and real-time internet data.

**🌟 Overview**

Unlike standard chatbots, this Agent doesn't just "chat." When asked a question about current events or complex topics, it:

Analyzes the intent of the query.

Decides if it needs external information.

Executes a search using the DuckDuckGo API.

Synthesizes the findings into a clear, cited response.

**🏗️ Technical Architecture**

The project follows a Modular Design Pattern, ensuring the code is scalable and easy to debug.

**tools.py:** Contains the DuckDuckGoSearchRun integration and any custom research utility functions.

**agent.py:** The "Orchestrator." It defines the LangGraph nodes and edges, managing the flow from the user to the search tool and back.

**application.py**: A reactive Streamlit dashboard that manages session state to provide a seamless, persistent chat experience.

**🛠️ Tech Stack**

**Frameworks:** LangChain & LangGraph (Stateful AI logic)

**LLM:** Llama 3.1 (8B Parameters)

**Hosting:** Local inference via Ollama

**Interface:** Streamlit (Python-based Web UI)

**Search Engine:** DuckDuckGo API

**🚀 Getting Started**

**Prerequisites**

Python 3.13+

Ollama installed and running (ollama pull llama3.1)

**🧠Core Logic:The Agentic Loop**

The heart of this projvext is the Stateful Graph.Instead of a linear inout->output flow,this agent uses a ciruclar logic:

**Chatbot Node:** Processes the message.

**Conditional Edge:** Asks that if the AI want to use a tool.

**Action:** If yes, it hits the Tool Node; if no, it finishes.

 

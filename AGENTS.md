# AGENTS.md: Smart Glossary Annotation System

## 1. Project Overview
The **Smart Glossary Annotation System** is an AI-powered accessibility tool designed as a "Digital Literacy Booster." It automates the identification, annotation, and explanation of complex technical and scientific terminology within educational documents. By leveraging multi-agent systems, it aims to help students and researchers navigate dense academic content effectively.

## 2. Agentic Workflow (Multi-Agent System)
The system utilizes an asynchronous communication protocol (A2A) between three core agents:

### A. ProcessorAgent (The Input Handler)
- **Role:** Handles document ingestion and input sanitization.
- **Responsibilities:** - Extracts text from PDF/DOCX files.
  - Performs input validation to prevent malicious prompt injection.
  - Prepares structured text chunks for analysis.

### B. AnalystAgent (The Core Engine)
- **Role:** Identifies and contextualizes terminology.
- **Responsibilities:**
  - Tokenizes input text and detects technical terms.
  - Determines if a term requires annotation based on the educational context.
  - Requests definitions from the `KnowledgeAgent` via A2A protocol.

### C. KnowledgeAgent (The Definition Fetcher)
- **Role:** Manages knowledge retrieval and user state.
- **Responsibilities:**
  - Connects to an MCP (Model Context Protocol) Server for accurate definitions.
  - Maintains a long-term memory (Vector DB) of user-specific preferences and frequently searched terms.
  - Adapts explanation complexity based on the user's learning profile.

## 3. Integration & Skills
- **MCP Integration:** Uses the Model Context Protocol to fetch definitions from external educational databases or customized knowledge bases.
- **Agent Skills:**
  - `glossary_search`: Retrieves verified definitions.
  - `context_adaptation`: Simplifies complex jargon based on the target academic level.
- **Guardrails:** Implements a security layer to filter hallucinations and ensure that annotations align with pedagogical standards.

## 4. Technical Specification
- **Track:** Agents for Good
- **Framework:** Google Agent Development Kit (ADK)
- **Communication Protocol:** A2A (Agent-to-Agent)
- **Memory Strategy:** Persistent User Context (Vector Database)
- **Security Posture:** Zero-Trust (Input validation & Egress governance)

## 5. Implementation Roadmap (Vibe Coding)
1. **Spec & Setup:** Define agent behaviors and interfaces.
2. **MCP Development:** Build the Glossary MCP Server for data interoperability.
3. **Agent Implementation:** Develop the `ProcessorAgent`, `AnalystAgent`, and `KnowledgeAgent` logic.
4. **Security Hardening:** Implement input validation and hallucination filters (Day 4 concepts).
5. **Evaluation:** Run test suites to measure term identification accuracy and annotation quality.

## 6. Project Goal
To serve as a high-velocity implementation engine that transforms dense academic documents into interactive, easy-to-understand learning materials, ensuring students can focus on comprehension rather than decoding vocabulary.
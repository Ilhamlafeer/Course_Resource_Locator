# 🎓 Course Resource Locator (CRL)

**Instant, Accurate Answers. Zero Database.**

The Course Resource Locator (CRL) is a lightweight, web-based Q&A application built to provide **immediate, hallucination-free answers** to course-related queries by leveraging the power of **Generative AI** and a novel, database-less architecture.

It solves the problem of students and staff wasting time navigating scattered PDFs, disparate portals, and complex systems to find simple course information


## ✨ Features

**Instant Answers:** Get real-time answers to questions about FAS degree programs, including details like **lecturer, credits, prerequisites, resources, objective, and title**
**Zero Database Architecture:** Utilizes **"Context Injection"** to eliminate the need for traditional database setup, management, and complex query logic, resulting in faster performance and simpler maintenance
**Factual Accuracy:** Enforces strict **AI Guardrails** (`SYSTEM_PROMPT`) to ensure the model *only* reasons over the provided course data, preventing hallucination and guaranteeing accuracy
**High Efficiency:** Eliminates network latency associated with database calls, ensuring speed
**Intuitive UI:** Built with **Streamlit** for rapid UI development and a clean, high-friction-free user experience


## ⚙️ How It Works: The "Context Injection" Core

The CRL's core logic is its **database-less architecture** built on Context Injection, which provides a fast, simple, and accurate way for the AI to process data

1.  **User Asks a Question:** The user inputs a query (e.g., "How many credits for Industrial Training?")
2.  **Data Fusion (Context Injection):** Instead of querying a database, the system dynamically injects the entire **course dataset (as a JSON dictionary)**, the user's question, and a **strict System Prompt (guardrails)** directly into the Large Language Model's (LLM) context.
3.  **AI Processes the Request:** **Google's Gemini 2.5 Flash** model reads the entire injected context. The System Prompt forces the model to act as a reliable data parser, following steps like identifying the course and field, and answering **ONLY** using the provided data.
4.  **Answer is Displayed:** The accurate, sourced result is immediately rendered to the user in a custom-styled green box.


## 🛠️ Technology Stack

The Course Resource Locator is built with a modern, efficient toolset:

**Language:** Python 3.13.2 [cite: 81, 134]
**AI Service:** Google **Gemini 2.5 Flash** via the Google Gemini API
**Web Framework:** **Streamlit** (for rapid UI development and deployment)
**Environment Management:** `python-dotenv` (for secure API key handling)
**Development:** Visual Studio Code / Google Colab

### 📊 Cost & Performance

The application is designed to be highly efficient and cost-effective

**Cost:** Entirely **Free** (using the no-credit-card Gemini API tier)
**Performance:** Capable of handling **15 Requests Per Minute** and **1,500 Requests Per Day**


## 🚀 Getting Started

1.  **Clone the repository.**
2.  **Install dependencies.**
3.  **Set up your Gemini API Key.**
4.  **Run the Streamlit app.**


## 🙋 Example Interaction

| **User Question** | **System Answer (Sourced from Injected Data)** |
| :--- | :--- |
| How many credits for Industrial Training | There are two courses titled 'Industrial Training'. Both CSH4226 and IT4226 have 6 credits. |
| Who is the lecturer for CSH4112? | [Factual Answer based on injected data] |

## 👨‍💻 Built By

**LM. [cite_start]ILHAM** for the course **CSH 4112**[cite: 3].

***

Would you like to draft the installation steps for the "Getting Started" section?

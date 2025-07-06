# SQL Agent with Gemini and Streamlit

This project is an interactive SQL Agent that uses [LangChain](https://python.langchain.com/), Google Gemini, and Streamlit to answer natural language questions about your database. It generates SQL queries, executes them, and returns answers in plain English.

---

## Features

- **Natural Language to SQL:** Converts user questions into SQL queries.
- **Database Execution:** Runs queries on a SQLite database (default: `Chinook.db`).
- **Conversational Interface:** User-friendly chat interface built with Streamlit.
- **Secure API Key Handling:** Uses a `.env` file for your Gemini API key.

---

## Setup

### 1. Clone the repository

```sh
git clone <your-repo-url>
cd <your-repo-folder>
```

### 2. Create and activate the conda environment

```sh
conda env create -f environment.yml
conda activate sqlagent
```

### 3. Add your Gemini API key

Create a `.env` file in the `sql_agent` directory with:

```
GOOGLE_API_KEY=your-gemini-api-key-here
```

**Note:**  
Your `.env` file is ignored by git for security.

### 4. Ensure you have the database

Place your `Chinook.db` (or another SQLite database) in the `sql_agent` directory.

---

## Running the App

```sh
cd sql_agent
streamlit run app.py
```

Open the provided URL in your browser to interact with the SQL Agent.

---

## File Structure

```
sql_agent/
│
├── agent.py         # Core logic for query generation and execution
├── app.py           # Streamlit chat interface
├── environment.yml  # Conda environment specification
├── requirements.txt # (Optional) Python dependencies for pip
├── .env             # (Not committed) Your Gemini API key
├── Chinook.db       # Example SQLite database
└── ...
```

---

## Usage

- Type your question in the chat (e.g., "How many employees are there?").
- The agent will generate a SQL query, execute it, and return the answer.

---


---

## Acknowledgements

- [LangChain](https://python.langchain.com/)
- [Streamlit](https://streamlit.io/)
- [Google Gemini](https://ai.google.dev/)
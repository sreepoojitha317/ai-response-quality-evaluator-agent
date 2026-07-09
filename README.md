# AI Response Quality Evaluator Agent

## Project Overview

The **AI Response Quality Evaluator Agent** project is divided into **four milestones**, with each milestone focusing on a specific stage of development.

This repository contains the implementation of **all 4 Milestones one by one **.

---

## Milestone 1: Data Processing, RAG Pipeline Setup and Basic User Interface 

The following tasks have been completed in this milestone:

* Collected and prepared the TruthfulQA and SQuAD datasets.
* Performed data preprocessing and cleaning.
* Split documents into chunks.
* Generated embeddings using OpenAI Embeddings.
* Created a ChromaDB vector database.
* Implemented document retrieval using LangChain.
* Developed the FastAPI backend.
* Built the frontend user interface with question, response type, response answer , using HTML, CSS, and JavaScript.

---

## Running the Project

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your OpenAI API key:

```text
OPENAI_API_KEY=your_api_key
```

Run the project:

```bash
python run.py
```

or

```bash
uvicorn app.main:app --reload
```

---

## Generated Files

The following files are **not included** in this repository because they are generated automatically during preprocessing and vector database creation:

* `data/processed/chunks.pkl`
* `data/processed/merged_dataset.csv`
* `data/processed/processed_dataset.csv`
* `data/chroma_db/`

These files will be generated automatically when the preprocessing and vector database creation pipeline is executed.

---

## Remaining Milestones

* **Milestone 2:** Response Evaluation Pipeline Enhancement
* **Milestone 3:** Performance Optimization and Additional Features
* **Milestone 4:** Final Integration, Testing, and Deployment

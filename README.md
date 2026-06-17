# 🧠 AI Research Assistant

An AI-powered Research Assistant that can analyze **YouTube videos** and **websites**, generate summaries, notes, flashcards, practice questions, and provide contextual question-answering using **RAG (Retrieval-Augmented Generation)**.

Built with **Streamlit**, **LangChain**, **Groq LLM**, **FAISS**, and **Hugging Face Embeddings**.

---

## 🚀 Features

### 📄 Content Summarization

Generate concise summaries from:

* YouTube videos
* Websites
* Blogs
* Articles

### ❓ Question Generation

Automatically generate practice and revision questions from the extracted content.

### 📝 Smart Notes

Create structured study notes from long-form content.

### 🎯 Flashcards

Generate quick revision flashcards for learning and retention.

### 💬 RAG-based Chat

Ask questions about the uploaded website or YouTube content and receive context-aware answers.

---

## 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* Groq (Llama 3.3 70B)
* Hugging Face Embeddings
* FAISS Vector Store
* BeautifulSoup
* YouTube Transcript API

---

## 📂 Project Structure

```text
AI_Research_Assistant/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── utils/
│   ├── youtube_loader.py
│   ├── website_loader.py
│   ├── rag.py
│   ├── helpers.py
│   └── prompts.py
│
└── .env
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone <your-repository-url>
cd ai-research-assistant
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

---

## 🧠 RAG Architecture

```text
Website / YouTube
        │
        ▼
 Content Extraction
        │
        ▼
 Text Chunking
        │
        ▼
 Embeddings
        │
        ▼
 FAISS Vector Store
        │
        ▼
 Retriever
        │
        ▼
 Groq LLM
        │
        ▼
 Context-Aware Answers
```

---

## 🌟 Future Improvements

* PDF Support
* Multi-Document Analysis
* Chat History Memory
* Export Notes as PDF
* Citation-Based Responses
* Multiple LLM Support

---


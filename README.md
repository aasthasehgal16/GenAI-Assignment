# GenAI Assignment - FAISS Vector Search

## Overview
This project implements a simple vector search system using FAISS. It simulates core Retrieval-Augmented Generation (RAG) concepts without using an LLM.

## Features
- Text embedding using NumPy
- Vector storage using FAISS
- Similarity search
- Basic retrieval system

## 📁 Project Structure

```
GenAI_Assignment/
│
├── main.py                  # Main execution script
├── dataset.py               # Sample dataset
├── results.txt              # Evaluation results
├── requirements.txt         # Dependencies
├── README.md                # Project documentation
│
├── screenshots/             # Output screenshots
│   ├── query_output.png
│   └── reingest.png
│
└── submission_template.docx # Final submission document
```

---

## 🧠 How It Works

1. **Dataset**
   - A small set of questions is used as input data.

2. **Embedding**
   - Each text is converted into a numerical vector using a custom function.

3. **FAISS Index**
   - Vectors are stored in a FAISS index (`IndexFlatL2`) for fast similarity search.

4. **Query Processing**
   - Input query → converted to vector → searched in FAISS

5. **Retrieval**
   - Top-k most similar results are returned.

6. **Evaluation**
   - A simulated judge compares correct vs incorrect answers to demonstrate bias.

---

## 🛠️ Setup Instructions

### 🔹 Prerequisites

- Python 3.8+
- pip

---

### 🔹 Installation

```bash
git clone [<my-repo-link>](https://github.com/aasthasehgal16/GenAI-Assignment)
cd GenAI_Assignment
pip install -r requirements.txt
```
---

```markdown id="y0t9yt"
```
---

## 👤 Author

**Aastha Sehgal**




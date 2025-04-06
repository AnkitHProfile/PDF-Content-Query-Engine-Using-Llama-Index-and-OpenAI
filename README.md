# 📄 PDF Content Query Engine using LlamaIndex & OpenAI

This project demonstrates how to build a powerful and reusable **PDF content query system** using **LlamaIndex (formerly GPT Index)** and **OpenAI’s GPT models**. It enables users to upload any PDF, automatically extract its content, index it, and perform natural language queries over the document with intelligent responses.

---

## 🎯 Objective

To allow users to:
- Upload and process PDFs in Google Colab
- Automatically extract and index the text
- Ask natural language questions and receive accurate answers
- Persist and reload the index for scalable, repeatable use

---

## 🚀 Features

- 🧠 **Natural Language Question Answering** over any uploaded PDF
- 📥 **Simple Upload and Renaming** of PDF files
- 📚 **Content Parsing** using `SimpleDirectoryReader`
- 📈 **Vector Store Indexing** with automatic document chunking & embedding
- 💾 **Persistent Storage** of the indexed data for reuse
- ✅ **OpenAI Integration** for intelligent language responses

---

## 🛠️ Tech Stack

| Component     | Technology                    |
|---------------|-------------------------------|
| Language Model| OpenAI GPT (via `llama-index`)|
| Indexing      | VectorStoreIndex (LlamaIndex) |
| Embeddings    | OpenAI Embeddings             |
| Parsing       | `SimpleDirectoryReader`       |
| Interface     | Google Colab Notebook         |
| Persistence   | LlamaIndex StorageContext     |

---

## 📦 Setup Instructions (Google Colab)

### 1. Install Dependencies

```python
!pip install llama-index openai
!pip install --upgrade llama-index
!pip install pypdf
```

### 2. Set Your OpenAI API Key

```python
import os
os.environ["OPENAI_API_KEY"] = "[Insert your API key here.]"
```

---

### 3. Upload Your PDF

```python
from google.colab import files
import os

uploaded = files.upload()
download_dir = "data"
new_filename = "Thoughts.pdf"

os.makedirs(download_dir, exist_ok=True)

for filename, file_content in uploaded.items():
    with open(os.path.join(download_dir, filename), 'wb') as f:
        f.write(file_content)
    os.rename(os.path.join(download_dir, filename), os.path.join(download_dir, new_filename))
```

---

### 4. Load and Index the PDF

```python
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()
```

---

### 5. Ask a Question

```python
response = query_engine.query("Insert your question here.")
from IPython.display import Markdown, display
display(Markdown(f"{response}"))
```

---

### 6. Persist the Index for Future Use

```python
index.storage_context.persist()
```

---

### 7. Reload the Index Anytime

```python
from llama_index.core import StorageContext, load_index_from_storage

storage_context = StorageContext.from_defaults(persist_dir="./storage")
index = load_index_from_storage(storage_context=storage_context)
```

---

## 🧪 Example Usage

```python
query_engine.query("Summarize the key arguments presented in the PDF.")
query_engine.query("What is the author's view on AI ethics?")
```

---

## 📁 Project Structure

```
PDF_Query_Engine/
├── PDF_Query_Engine.ipynb       # Colab notebook
├── data/
│   └── Thoughts.pdf             # Uploaded and renamed PDF
├── storage/                     # Persisted index files
```

---

## ✅ Conclusion

This project offers a streamlined way to query custom PDFs using natural language, combining the power of OpenAI’s language models and LlamaIndex’s retrieval capabilities. It's perfect for:
- Researchers analyzing academic papers
- Students summarizing readings
- Professionals reviewing reports

---

## 👨‍💻 Contributor

**Ankit Hiremath**  
GitHub: [AnkitHProfile](https://github.com/AnkitHProfile)

# FastAPI CRUD API
## 📌 Project Overview

This project implements a basic CRUD API for managing notes using FastAPI and SQLAlchemy.  
It follows a clean project structure and demonstrates backend development best practices.

---

## 🚀 Features

- FastAPI for high-performance APIs
- SQLAlchemy ORM for database operations
- SQLite database (easy local setup)
- Pydantic schemas for data validation
- Automatic API documentation (Swagger & ReDoc)

---

## 📁 Project Structure

```
fastapi-crud-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── note.py
│
├── requirements.txt
├── example.env
├── README.md
└── .gitignore
```


---
## ⚙️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/suhani996/fastapi-crud-api.git
cd fastapi-crud-api
```
2️⃣ Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```
3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
▶️ Run the Application
```bash
uvicorn app.main:app --reload
```
Server will start at:
http://127.0.0.1:8000

📘 API Documentation
Swagger UI → http://127.0.0.1:8000/docs

ReDoc → http://127.0.0.1:8000/redoc

🛠️ CRUD Operations
Create a record

Read all records

Read a single record by ID

Update a record

Delete a record

🧪 Technologies Used
Python 3

FastAPI

SQLAlchemy

SQLite

Pydantic

Uvicorn

👩‍💻 Author
Suhani Pendyala

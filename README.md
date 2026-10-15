# 🎓 FastAPI Student Management API

A beginner-friendly Student Management REST API built with **FastAPI, Python, and Pydantic**. This project focuses on request validation, CRUD operations, HTTP exception handling, and building structured backend APIs.

## 🚀 Features

- Create student records
- Retrieve student information
- Update student records
- Delete student records
- Validate request data using Pydantic
- Prevent duplicate student IDs
- Handle errors using HTTP status codes
- Test endpoints using interactive Swagger UI
- Manage records using Python dictionaries

## 🛠️ Tech Stack

- **Python** — Programming language
- **FastAPI** — API development framework
- **Pydantic** — Data validation and schema definition
- **Uvicorn** — ASGI server
- **Swagger UI** — Interactive API documentation

## 📁 Project Structure

```text
fastapi-student-management/
├── main.py
├── schema.py
├── model_services.py
├── requirements.txt
├── README.md
└── .gitignore
```

**File descriptions:**
- `main.py` — FastAPI application and API routes.
- `schema.py` — Pydantic models and validation rules.
- `model_services.py` — Student management logic and duplicate ID checking.
- `requirements.txt` — Python dependencies.
- `README.md` — Project documentation.

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/fastapi-student-management.git
cd fastapi-student-management
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create a virtual environment

```bash
python -m venv myenv
```

Activate it on Windows PowerShell:

```powershell
.\myenv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python -m uvicorn main:app --reload
```

The API will run locally at:

`http://127.0.0.1:8000`

## 📚 API Documentation

FastAPI automatically generates interactive documentation.



Use Swagger UI to send requests and inspect API responses.

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/students` | Retrieve all students |
| GET | `/students/{student_id}` | Retrieve a student by ID |
| POST | `/students` | Create a new student |
| PUT | `/students/{student_id}` | Update a student |
| DELETE | `/students/{student_id}` | Delete a student |

*Make sure these endpoints match your actual implementation before publishing.*

## 📝 Example: Create a Student

**Method:** `POST`

**Endpoint:** `/students`

Request body:

```json
{
  "student_id": 101,
  "name": "Rakesh",
  "age": 20
}
```

Example response:

```json
{
  "student_id": 101,
  "name": "Rakesh",
  "age": 20
}
```

The exact response depends on your implementation.

## ✅ Data Validation

Pydantic validates incoming data according to the defined model.

Examples of validation rules:
- Required fields must be provided.
- Fields must have the expected data types.
- Custom constraints can restrict values.
- Invalid request data produces a validation error.

## ⚠️ HTTP Status Codes

| Status Code | Description |
|---|---|
| `200 OK` | Request successful |
| `201 Created` | Student created successfully |
| `404 Not Found` | Student does not exist |
| `409 Conflict` | Student ID already exists |
| `422 Unprocessable Entity` | Request validation failed |

## 🧠 Key Learnings

- Creating REST APIs with FastAPI
- Defining Pydantic models
- Validating request fields
- Handling HTTP exceptions
- Implementing CRUD operations
- Using dictionaries for temporary storage
- Separating routes, schemas, and business logic
- Testing APIs using Swagger UI

## 🔮 Future Improvements

- Integrate MySQL for persistent storage
- Add automated tests using Pytest
- Implement authentication and authorization
- Improve error handling and response schemas
- Deploy the API to a cloud platform

## 👨‍💻 Author

**Rakesh Verma**

- GitHub: [@hey-rakesh](https://github.com/hey-rakesh)


---

⭐ If you find this project useful, consider giving the repository a star!

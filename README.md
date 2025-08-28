# 🎓 Student Management API

A lightweight Flask REST API for managing student records with PostgreSQL database integration.

## 🚀 Quick Start

```bash
# Clone and setup
git clone <your-repo>
cd student-management-api
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
# Create .env file with your PostgreSQL credentials
DB_HOST=localhost
DB_NAME=your_database_name
DB_USER=your_username
DB_PASSWORD=your_password
DB_PORT=5432

# Run the API
python app.py
```

API will be available at: `http://localhost:5000`

## 📋 API Endpoints

| Method | Endpoint | Description | Response |
|--------|----------|-------------|----------|
| `GET` | `/` | Welcome message | JSON message |
| `GET` | `/students` | Get all students (ordered by ID desc) | Array of students |
| `POST` | `/students` | Add new student | Created student object |

## Testing with Thunder Client (VS Code)

### GET Students
```
Method: GET
URL: http://localhost:5000/students
Headers: (none required)
```

### POST New Student
```
Method: POST
URL: http://localhost:5000/students
Headers: Content-Type: application/json
Body (JSON):
{
  "name": "Alice Johnson",
  "age": 21,
  "email": "alice@email.com",
  "grade": "A-"
}
```

### Expected Responses

**GET /students:**
```json
[
  {
    "id": 1,
    "name": "Alice Johnson",
    "age": 21,
    "email": "alice@email.com",
    "grade": "A-"
  }
]
```

**POST /students (Success - 201):**
```json
{
  "id": 2,
  "name": "Alice Johnson",
  "age": 21,
  "email": "alice@email.com",
  "grade": "A-"
}
```

**POST /students (Error - 400):**
```json
{
  "error": "missing fields: name, age, email required"
}
```

## 🗄️ Database Schema

The API automatically creates this PostgreSQL table:

```sql
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);
```

## 📦 Dependencies

```
blinker==1.9.0
click==8.2.1
colorama==0.4.6
Flask==3.1.2
itsdangerous==2.2.0
Jinja2==3.1.6
MarkupSafe==3.0.2
psycopg2-binary==2.9.10
python-dotenv==1.1.1
Werkzeug==3.1.3
```

## 🔒 Features

**Auto table creation** - Database schema created automatically  
**Environment config** - Secure credential management with .env  
**Input validation** - Required fields validation  
**SQL injection protection**
# ABUDevs API

A scalable Flask REST API built for the ABUDevs community platform to manage student registrations, blogs, events, and admin authentication.

---

## 🚀 Features

- ✅ **JWT Authentication** (Admin login and access control)
- 📚 **Blog Management** (CRUD for admin)
- 📅 **Event Management** (CRUD for admin)
- 👨‍🎓 **Student Registration** (Public form + student list)
- 🧪 **Pytest Test Suite** for routes and models
- 🌍 **Postman API Documentation** with authentication

---

## 📁 Project Structure

```

abudevs\_api/
│
├── app/
│   ├── **init**.py
│   ├── models/
│   │   ├── blog.py
│   │   ├── event.py
│   │   ├── student.py
│   │   └── user.py
│   ├── routes/
│   │   ├── auth.py
│   │   ├── blogs.py
│   │   ├── events.py
│   │   └── students.py
│   └── utils/
│       └── auth\_helpers.py
│
├── tests/
│   ├── **init**.py
│   ├── conftest.py
│   ├── test\_auth.py
│   ├── test\_blogs.py
│   ├── test\_events.py
│   └── test\_students.py
│
├── migrations/
│
├── .env
├── config.py
├── run.py
└── README.md

````

---

## 🛠️ Setup & Installation

### 1. Clone Repo

```bash
git clone https://github.com/yourusername/abudevs_api.git
cd abudevs_api
````

### 2. Create Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate  # For Linux/macOS
# OR
.venv\Scripts\activate  # For Windows
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file at the project root:

```
SECRET_KEY=your-secret-key
JWT_SECRET_KEY=your-jwt-secret
DATABASE_URL=sqlite:///dev.db  # or your Supabase URI
```

---

## 🧪 Running the API Locally

```bash
export FLASK_APP=run.py
export FLASK_ENV=development
flask run
```

Visit: `http://localhost:5000`

---

## 🧪 Run Tests with Pytest

```bash
pytest
```

---

## 🔗 API Endpoints Summary

| Endpoint             | Method | Access    | Description             |
| -------------------- | ------ | --------- | ----------------------- |
| `/auth/register`     | POST   | Public    | Register admin user     |
| `/auth/login`        | POST   | Public    | Login and get JWT token |
| `/auth/me`           | GET    | Protected | Get current user        |
| `/students/register` | POST   | Public    | Register a new student  |
| `/students/`         | GET    | Public    | Get all students        |
| `/students/<id>`     | GET    | Public    | Get single student      |
| `/students/<id>`     | PUT    | Protected | Update student by ID    |
| `/students/<id>`     | DELETE | Protected | Delete student by ID    |
| `/blogs/`            | POST   | Protected | Create blog             |
| `/blogs/`            | GET    | Public    | Get all blogs           |
| `/blogs/<id>`        | GET    | Public    | Get blog by ID          |
| `/blogs/<id>`        | PUT    | Protected | Update blog             |
| `/blogs/<id>`        | DELETE | Protected | Delete blog             |
| `/events/`           | POST   | Protected | Create event            |
| `/events/`           | GET    | Public    | Get all events          |
| `/events/<id>`       | GET    | Public    | Get event by ID         |
| `/events/<id>`       | PUT    | Protected | Update event            |
| `/events/<id>`       | DELETE | Protected | Delete event            |

---

## 📬 Example JSON Payloads

### 🔐 Register/Login (Admin)

```json
{
  "username": "admin",
  "password": "adminpass"
}
```

### 📝 Blog Creation

```json
{
  "track": "Web Dev",
  "title": "Building REST APIs",
  "subtitle": "A beginner's guide",
  "body": "This is a tutorial...",
  "author": "Admin",
  "author_position": "Mentor",
  "date": "2025-06-04",
  "hashtags": "#api,#flask"
}
```

### 📅 Event Creation

```json
{
  "title": "Tech Talk",
  "description": "Exploring AI and ML",
  "venue": "Main Auditorium",
  "date": "2025-06-15",
  "time": "14:00:00"
}
```

### 👨‍🎓 Student Registration

```json
{
  "first_name": "Ada",
  "last_name": "Lovelace",
  "email": "ada@example.com",
  "student_id": "U12345",
  "department": "Computer Science",
  "level": "400"
}
```


## 🚀 Deployment (Supabase + Render/Railway)

1. Update `.env` with your **Supabase DB URI**:

   ```env
   DATABASE_URL=postgresql://username:password@host:port/dbname
   ```

2. Set `FLASK_ENV=production` before deploying.

3. Use `gunicorn` in production:

   ```bash
   gunicorn 'app:create_app("production")'
   ```

---

## 📄 License

MIT License © 2025 ABUDevs

---

# 📝 To-Do List Web Application

A full-stack To-Do List web application built with **Python, Flask, SQLite, HTML, CSS, and Git**.

The application allows users to create an account, securely log in, manage personal tasks, mark tasks as completed, delete tasks, and view their profile and task dashboard.

🔗 **Live Demo:** https://tdl-project.onrender.com

---

## 📌 Features

- 🔐 User registration and login
- 🔒 Password hashing for secure password storage
- 👤 Individual user accounts
- ➕ Add new tasks
- ✅ Mark tasks as completed
- 🗑️ Delete individual tasks
- 🧹 Clear all tasks
- 📊 Task dashboard
- 👤 User profile page
- 🚪 Logout functionality
- 💾 Persistent SQLite database
- 📱 Simple and responsive web interface
- ☁️ Deployed and accessible online using Render

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python** | Backend programming |
| **Flask** | Web framework and routing |
| **SQLite** | Database |
| **HTML** | Web page structure |
| **CSS** | Styling and layout |
| **Jinja2** | Dynamic HTML templating |
| **Werkzeug** | Password hashing |
| **Git** | Version control |
| **GitHub** | Source code hosting |
| **Render** | Application deployment |

---

## 🏗️ Project Structure

```text
tdl_project/
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   └── profile.html
│
├── app.py
├── better_sorce.py
├── requirements.txt
├── tasks.db
└── README.md
```

---

## ⚙️ How It Works

The application follows a simple full-stack architecture:

```text
User
  │
  ▼
HTML / CSS Interface
  │
  ▼
Flask Application
  │
  ├── Authentication
  ├── Task Management
  └── User Management
  │
  ▼
SQLite Database
```

### Authentication

When a user registers:

1. The username is stored in the database.
2. The password is hashed using Werkzeug.
3. The hashed password is stored instead of the original password.

During login, the submitted password is checked against the stored hash.

### Task Management

Each task is associated with the logged-in user's ID.

This means users only see and modify their own tasks.

Tasks can be:

- Added
- Marked as completed
- Deleted
- Cleared

---

## 🗄️ Database

The application uses **SQLite** as its database.

### `users`

Stores registered users.

| Column | Description |
|--------|-------------|
| `id` | Unique user ID |
| `username` | Username |
| `password` | Hashed password |

### `tdl_table`

Stores user tasks.

| Column | Description |
|--------|-------------|
| `num` | Unique task ID |
| `work` | Task description |
| `date` | Task creation date and time |
| `status` | Task status |
| `user_id` | ID of the user who created the task |

The `user_id` connects tasks to their respective users.

---

## 🚀 Running the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/FunDood155/tdl_project.git
```

### 2. Enter the project directory

```bash
cd tdl_project
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### Git Bash

```bash
source venv/Scripts/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python app.py
```

The application will normally be available at:

```text
http://127.0.0.1:5000
```

Open that address in your browser.

---

## 🌐 Live Demo

The application is deployed on Render:

### 👉 https://tdl-project.onrender.com

> **Note:** The live demo is hosted using Render's free web service. Free services may spin down after periods of inactivity, so the first request after inactivity can take longer than subsequent requests.

---

## 🔄 Deployment

The project is connected to GitHub and deployed using Render.

The general deployment flow is:

```text
Code Changes
     │
     ▼
   Git
     │
     ▼
  GitHub
     │
     ▼
   Render
     │
     ▼
 Live Web Application
```

Changes pushed to the connected GitHub branch can trigger a new Render deployment. :contentReference[oaicite:2]{index=2}

For a Flask application, Render uses the repository's dependencies and a production server such as Gunicorn to run the application. :contentReference[oaicite:3]{index=3}

---

## 🔐 Security

The application includes basic authentication security practices:

- Passwords are hashed using Werkzeug.
- Passwords are not stored as plain text.
- User sessions are used to maintain login state.
- Database queries use parameterized values to reduce SQL injection risk.
- Users can only access their own tasks.

> This project is primarily an educational project and is not intended to represent a production-grade authentication system.

---

## 📚 What I Learned

Building this project helped me practice:

- Python programming
- Flask routing
- HTTP GET and POST requests
- HTML forms
- Jinja2 templates
- CSS styling
- SQLite database operations
- SQL queries
- CRUD operations
- User authentication
- Password hashing
- Session management
- Git and GitHub
- Deployment of a Flask application
- Debugging full-stack applications

---

## 🔮 Future Improvements

Possible improvements for future versions:

- [ ] Edit existing tasks
- [ ] Task categories
- [ ] Task priorities
- [ ] Due dates
- [ ] Search and filtering
- [ ] Improved mobile UI
- [ ] Better authentication and session security
- [ ] PostgreSQL for production database hosting
- [ ] User profile customization
- [ ] REST API
- [ ] Better deployment configuration

---

## 👨‍💻 Author

**FunDood155**

GitHub:  
https://github.com/FunDood155

---

## 📄 License

This project is currently intended as a personal/educational project.

# Intelligent Quiz Management System 

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Django](https://img.shields.io/badge/Django-5.x-green)
![Status](https://img.shields.io/badge/Status-Completed-success)
![License](https://img.shields.io/badge/License-Educational-orange)

The **Intelligent Quiz Management System** is a full-stack web application built using **Django** that enables users to securely register, attempt quizzes, track scores, and view rankings on a leaderboard.
The project focuses on clean architecture, secure authentication, and scalable quiz management.

This application is ideal for **online assessments, learning platforms, and educational institutions**.

---

## 🧠 Key Highlights

* Clean **MVC-based architecture** using Django
* Secure authentication with Django Auth
* Modular and scalable app structure
* User-friendly and responsive UI
* Git & GitHub best practices followed

---

## 🚀 Features

### 👤 User Module

* User Registration & Login
* Secure Logout
* Password Reset via Email
* Profile Management

### 📝 Quiz Module

* Category-wise quizzes
* Multiple questions per quiz
* Automatic score calculation
* Quiz attempt tracking

### 🏆 Performance Tracking

* Leaderboard with rankings
* Individual score history
* Attempt-based performance evaluation

---

## 🛠️ Tech Stack

| Layer           | Technology           |
| --------------- | -------------------- |
| Backend         | Python, Django       |
| Frontend        | HTML, CSS, Bootstrap |
| Database        | SQLite               |
| Authentication  | Django Auth          |
| Version Control | Git, GitHub          |

---

## 📂 Project Architecture

```
intelligent_quiz_management_system/
│
├── intelligent_quiz/
│   ├── quiz/               # Quiz logic & views
│   ├── users/              # User profiles & auth
│   ├── quiz_system/        # Project settings
│   ├── templates/          # HTML templates
│   └── static/             # CSS & assets
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Local Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/smriti121/intelligent_quiz_management_system.git
cd intelligent_quiz_management_system
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Database Migration

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Run Server

```bash
python manage.py runserver
```

Access the application at:

```
http://127.0.0.1:8000/
```

---

## 🔐 Admin Panel Access

Create admin user:

```bash
python manage.py createsuperuser
```

Admin Dashboard:

```
http://127.0.0.1:8000/admin/
```

---

## 📈 Future Enhancements

* ⏱️ Timed quizzes
* 📊 Analytics dashboard
* 📧 Email notifications
* 🧪 AI-based question generation
* ☁️ Cloud deployment (AWS / Render)

---

## 👩‍💻 Author

**Smriti Kumari**
Aspiring Full Stack Developer
GitHub: [https://github.com/smriti121](https://github.com/smriti121)

---

## 📜 License

This project is developed for **educational and learning purposes**.

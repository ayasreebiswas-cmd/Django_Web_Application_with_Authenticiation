# Django Web Application with Authentication

A **Django-based task management web application** designed with full user authentication, role-based permissions, and real-time task tracking. Developed as part of the **Codveda Technology** Python Development Internship.

## Features

* 🔐 User registration, login, and secure logout


* 🔑 Built-in password hashing and security


* 📧 Password reset functionality via console email backend


* 👥 Role-based access control (Admin vs. Regular Users)


* 📊 Interactive dashboard showing total and completed task metrics
* 📝 Complete Task CRUD (Create, Read, Update, Delete) management


* 🎨 Modern and responsive user interface

## Technologies Used

* **Python**
* **Django**

* **HTML5 / CSS3**
* **SQLite3 Database**
* **Git & GitHub**


## Project Structure

```text
Django_Web_Application_with_Authentication/
│
├── taskmanager/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── tasks/
│   ├── templates/
│   │   └── tasks/
│   │       ├── base.html
│   │       ├── dashboard.html
│   │       ├── login.html
│   │       ├── password_reset.html
│   │       ├── register.html
│   │       └── task_form.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── db.sqlite3
├── manage.py
├── .gitignore
├── requirements.txt
└── venv/

```

> **Note:** `db.sqlite3` and `venv/` should not be committed to GitHub.

## How It Works

1. **User Authentication:** Users sign up through the registration interface. Passwords are encrypted before storage.


2. **Role Determination:** Custom user models dynamically distinguish Admin users from Regular users.


3. **Task Assignment:** Admins create tasks and assign them to specific team members.


4. **Dashboard View:** Regular users view only their assigned tasks, while Admins see overall system statistics and all pending/completed tasks.



## Security & Best Practices

The `.gitignore` file should contain:

```text
venv/
*.pyc
__pycache__/
db.sqlite3
.env

```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Django_Web_Application_with_Authentication.git

```

### 2. Open the Project Directory

```bash
cd Django_Web_Application_with_Authentication/taskmanager

```

### 3. Create a Virtual Environment

On Windows:

```cmd
python -m venv venv

```

### 4. Activate the Virtual Environment

```cmd
venv\Scripts\activate

```

### 5. Install Dependencies

```cmd
pip install django

```

Generate the requirements file:

```cmd
pip freeze > requirements.txt

```

### 6. Apply Database Migrations

```cmd
python manage.py makemigrations tasks
python manage.py migrate

```

## Running the Application

Activate the virtual environment:

```cmd
venv\Scripts\activate

```

Start the development server:

```cmd
python manage.py runserver

```

Open your browser and navigate to:

```text
http://127.0.0.1:8000/

```

## Application Routes

* **Dashboard:** `GET /dashboard/`

* **User Login:** `GET /login/`

* **User Registration:** `GET /register/`

* **Task Creation (Admin):** `GET /create-task/`

* **Password Reset:** `GET /password-reset/`


## GitHub Workflow

After making changes:

```cmd
git status
git add .
git commit -m "Update Django application"
git push

```

## Future Improvements

* 🔔 Email notifications on task assignment


* 📈 Historical task completion charts
* 📁 Attachment/file sharing per task
* 🚀 Cloud deployment (Heroku / AWS)

## Author

Ayasree Biswas

## License

This project is intended for educational and internship assessment purposes.

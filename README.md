# 📌 Django Internship Assignment: API, Celery & Telegram Bot

This project is a comprehensive Django application built for an internship assignment. It demonstrates a wide range of backend development skills, including creating a RESTful API, handling asynchronous tasks, integrating with external services like Telegram, and following best practices for security and code management.

## ✨ Features

-   **RESTful API**: Built with Django REST Framework, featuring both public and protected endpoints.
-   **JWT Authentication**: Secure, stateless API authentication using `djangorestframework-simplejwt`.
-   **Asynchronous Tasks**: Celery is integrated with Redis as a message broker to handle long-running background tasks, such as sending welcome emails.
-   **Telegram Bot Integration**: A functional Telegram bot that interacts with users and stores their information in the Django database.
-   **Environment-based Configuration**: All sensitive data (like secret keys and tokens) is managed outside of version control using environment variables via `django-environ`.
-   **Clean Code & Structure**: The project follows best practices for code quality, documentation, and version control with Git.

---

## 🛠️ Setup Instructions

Follow these steps to get a local copy of the project up and running.

### 1. Prerequisites

-   Python 3.8+
-   Redis
-   An active Telegram account and a Bot Token from [BotFather](https://t.me/botfather).

### 2. Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/CtrlAltDefeattt/django-internship-project.git
    cd django-internship-project
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    Create a file named `.env` in the project root. You can copy the example structure below.
    ```bash
    # On macOS/Linux
    cp .env.example .env

    # On Windows, you can manually create the file.
    ```
    See the [Environment Variables](#-environment-variables) section for details on what to include.

5.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

6.  **Create a superuser to access the Django Admin:**
    ```bash
    python manage.py createsuperuser
    ```

---

## 🔐 Environment Variables

Create a `.env` file in the project's root directory and add the following variables. Do **not** commit this file to version control.

```env
# Django Core Settings
SECRET_KEY='your-super-secret-key-goes-here'
DEBUG=True

# Database URL (using SQLite for local development)
DATABASE_URL='sqlite:///db.sqlite3'

# Telegram Bot Token
TELEGRAM_BOT_TOKEN='your-telegram-bot-token-from-botfather'
```

---

## 🚀 How to Run Locally

This project requires multiple services to be running simultaneously. Open a new terminal for each command.

1.  **Start the Redis Server:**
    (This command may vary based on your operating system and installation method.)
    ```bash
    redis-server
    ```

2.  **Start the Celery Worker:**
    The Celery worker listens for and executes background tasks.
    ```bash
    celery -A core worker -l info
    ```

3.  **Start the Django Development Server:**
    This runs the main web application.
    ```bash
    python manage.py runserver
    ```

4.  **Start the Telegram Bot:**
    This command starts polling Telegram for new messages.
    ```bash
    python manage.py startbot
    ```

---

## 🔁 Celery Usage

Celery is used to run a background task that sends a welcome email to a new user upon registration. This ensures the registration process is fast and doesn't get blocked by email-sending delays.

-   **Task Definition**: The task `send_welcome_email_task` is defined in `api/tasks.py`.
-   **Trigger**: The task is triggered automatically by a Django signal (`post_save`) in `api/signals.py` whenever a new `User` object is created.
-   **Running the Worker**: To process these tasks, the Celery worker must be running (see the command in the "How to Run Locally" section).

---

## 🤖 Telegram Bot

The integrated Telegram bot listens for the `/start` command.

-   **Functionality**: When a user sends `/start`, the bot extracts their Telegram `chat_id` and `username` and saves them to the `TelegramUser` model in the database.
-   **How to Test**:
    1.  Run the `startbot` management command: `python manage.py startbot`.
    2.  Open Telegram and send the `/start` message to your bot.
    3.  The bot will reply with a welcome message.
    4.  You can verify that the user was saved by checking the Django Admin panel at `http://127.0.0.1:8000/admin/telegram_bot/telegramuser/`.

---

## 🔐 Authentication

Authentication is handled by JWT (JSON Web Tokens). To access protected endpoints, you must first obtain a token and then include it in the `Authorization` header of your requests.

1.  **Get an Access Token:**
    Send a `POST` request to `/api/token/` with your user credentials.
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"username":"your_username","password":"your_password"}' http://127.0.0.1:8000/api/token/
    ```
    The response will contain your `access` and `refresh` tokens.

2.  **Access Protected Endpoints:**
    Include the `access` token in the `Authorization` header as a Bearer token.
    ```bash
    curl -H "Authorization: Bearer <your_access_token>" http://127.0.0.1:8000/api/protected/
    ```

---

## 🧪 API Endpoints

### User Registration

-   **Method**: `POST`
-   **URL**: `/api/register/`
-   **Auth Required**: No
-   **Body**:
    ```json
    {
        "username": "newuser",
        "email": "newuser@example.com",
        "password": "strongpassword"
    }
    ```

### Public Endpoint

-   **Method**: `GET`
-   **URL**: `/api/public/`
-   **Auth Required**: No
-   **Example Response**:
    ```json
    {
        "message": "This is a public endpoint."
    }
    ```

### Protected Endpoint

-   **Method**: `GET`
-   **URL**: `/api/protected/`
-   **Auth Required**: Yes (JWT Bearer Token)
-   **Example Response**:
    ```json
    {
        "message": "Hello, your_username! This is a protected endpoint."
    }
    ```

---

## 📁 Project Structure

```
django-internship-project/
├── .gitignore
├── README.md
├── api/
├── core/
│   ├── __init__.py
│   ├── asgi.py
│   ├── celery.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── telegram_bot/
```

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE). 
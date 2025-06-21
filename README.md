# Django REST API and Telegram Bot

This project is a comprehensive Django application featuring a RESTful API with public and protected endpoints, JWT-based authentication, background tasks with Celery and Redis, and a Telegram bot integration.

## Features

- **Django REST Framework:** For building robust APIs.
- **JWT Authentication:** Secure, stateless authentication using `djangorestframework-simplejwt`.
- **Celery:** Asynchronous task processing for background jobs like sending emails.
- **Redis:** Message broker for Celery.
- **Telegram Bot:** A simple bot that saves user information to the database.
- **Production-Ready Settings:** Uses `django-environ` to manage environment variables.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8+
- Redis
- An active Telegram account

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd <your-repo-name>
    ```

2.  **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: We will generate the `requirements.txt` file in the next step.)*

4.  **Set up environment variables:**
    Create a `.env` file in the project root by copying the example:
    ```bash
    cp .env.example .env
    ```
    Then, fill in the variables in your new `.env` file.

5.  **Run database migrations:**
    ```bash
    python manage.py migrate
    ```

6.  **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

## Environment Variables

To run this project, you will need to add the following environment variables to your `.env` file:

- `SECRET_KEY`: A long, random string for Django's security.
- `DEBUG`: Set to `True` for development, `False` for production.
- `DATABASE_URL`: The connection string for your database (e.g., `sqlite:///db.sqlite3` for local development).
- `TELEGRAM_BOT_TOKEN`: Your token from Telegram's BotFather.

Here is an example `.env.example` file:

```
SECRET_KEY='your-super-secret-key'
DEBUG=True
DATABASE_URL='sqlite:///db.sqlite3'
TELEGRAM_BOT_TOKEN='your-telegram-bot-token'
```

## Running the Project Locally

To run the full application, you will need to start three services in separate terminal windows.

1.  **Start the Redis Server:**
    (This depends on your OS and installation method)
    ```bash
    redis-server
    ```

2.  **Start the Celery Worker:**
    ```bash
    celery -A core worker -l info
    ```

3.  **Start the Django Development Server:**
    ```bash
    python manage.py runserver
    ```

4.  **Start the Telegram Bot:**
    ```bash
    python manage.py startbot
    ```

## API Documentation

*(This section can be expanded with more details about your API endpoints.)*

### Authentication

-   **Get JWT Token:** `POST /api/token/`
-   **Refresh JWT Token:** `POST /api/token/refresh/`

### Endpoints

-   **Public:** `GET /api/public/`
-   **Protected:** `GET /api/protected/` (Requires `Authorization: Bearer <token>`)
-   **Register:** `POST /api/register/`

---
This `README.md` provides a solid foundation. You can add more specific details as your project grows. 
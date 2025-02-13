# Django OTP Authentication

## 📌 Описание проекта
Django OTP Authentication — это безопасная система аутентификации с двухфакторной авторизацией (OTP, One-Time Password) для веб-приложений, построенная на основе Django.

## 🚀 Стек технологий
- **Python** 3.10
- **Django** (основной фреймворк)
- **Django REST Framework** (API)
- **PostgreSQL** (база данных)
- **Docker** + **Docker Compose** (контейнеризация)

## 📦 Установка и запуск

### 1️⃣ Создаем .env файл
Создайте файл `.env` в корне проекта и скопируйте из .env.example переменные окружения:
```ini
DJANGO_SECRET_KEY=your_secret_key
DEBUG=True
...
!!! Не забудьте указать свои данные
```

### 3️⃣ Запускаем проект в Docker
```bash
docker-compose up --build -d
```
Это создаст и запустит контейнеры с Django, PostgreSQL

### 4️⃣ Создание суперпользователя
```bash
docker-compose exec web python manage.py createsuperuser
```

### 5️⃣ Доступ к приложению
После успешного запуска сервер будет доступен по адресу:
```
http://localhost:8000
```

## 🛠 API Эндпоинты
- **POST** `/api/send-otp-code/` – Отправка код подтверждения
- **POST** `/api/auth/` – Вход (Регистрация)

## 🛠 Запуск тестов(Pytest)
```shell
pytest .
```


## 📝 Лицензия
Этот проект распространяется под лицензией MIT.

---
✨ Разработано с любовью ❤️ и безопасностью 🔒


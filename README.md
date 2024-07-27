# IoT Management Application

## Опис

Цей додаток призначений для управління IoT пристроями. Він використовує PostgreSQL для збереження даних і aiohttp для створення асинхронного API.

## Налаштування

1. Встановіть необхідні пакети:
    ```bash
    pip install requirements.txt
    ```

2. Налаштуйте PostgreSQL:
    ```sql
    CREATE DATABASE iot_management;
    ```

3. Встановіть ваші облікові дані для бази даних в `models.py`:
    ```python
    db = PostgresqlDatabase('iot_management', user='your_username', password='your_password', host='localhost', port=5432)
    ```

4. Створіть таблиці у базі даних:
    ```bash
    python -m models
    ```

5. Запустіть додаток:
    ```bash
    python app.py
    ```

## Використання

API підтримує наступні операції CRUD для пристроїв:

- **Додати користувача** (POST `/users`)
- **Додати локацію** (POST `/locations`)
- **Додати пристрій** (POST `/devices`)
- **Отримати всі пристрої** (GET `/devices`)
- **Отримати пристрій за ID** (GET `/devices/{id}`)
- **Оновити пристрій за ID** (PUT `/devices/{id}`)
- **Видалити пристрій за ID** (DELETE `/devices/{id}`)

## Приклади запитів

### Додавання пристрою
```json
POST /devices
{
    "name": "Device1",
    "type": "Sensor",
    "login": "device_login",
    "password": "device_password",
    "location": 1,
    "api_user": 1
}

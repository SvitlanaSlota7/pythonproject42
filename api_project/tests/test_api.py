import pytest
from fastapi.testclient import TestClient

# Імпортуємо наш екземпляр додатка FastAPI
from src.main import app, db_notes

# Створюємо тестовий клієнт. Він імітує реальні HTTP-запити до нашого API
client = TestClient(app)


@pytest.fixture(autouse=True)
def clear_database():
    """Очищення БД перед кожним тестом"""
    global db_notes
    db_notes.clear()
    # Скидаємо лічильник id (оскільки в main.py ми використовуємо global,
    # для простоти прикладу імпортуємо і скидаємо лічильник прямо в модулі,
    # для інтеграційних тестів головне — чиста БД
    import src.main
    src.main.next_id = 1


def test_create_note_integration():
    """Інтеграційний тест: створення нотатки через POST-запит"""
    # 1. Надсилаємо POST-запит із JSON-даними
    response = client.post("/notes", json={"text": "Привітання з інтеграційного тесту"})

    # 2. Перевіряємо, чи повернувся правильний HTTP статус-код (201)
    assert response.status_code == 201

    # 3. Перевіряємо JSON-відповідь сервера
    data = response.json()
    assert data["id"] == 1
    assert data["text"] == "Привітання з інтеграційного тесту"


def test_get_note_success_integration():
    """Інтеграційний тест: успішне отримання нотатки через GET-запит"""
    # Спочатку створюємо нотатку, щоб вона з'явилася в системі
    client.post("/notes", json={"text": "Тестова нотатка для GET"})

    # Робимо GET-запит для отримання цієї нотатки (її ID має бути 1)
    response = client.get("/notes/1")

    assert response.status_code == 200
    assert response.json() == {"id": 1, "text": "Тестова нотатка для GET"}


def test_get_note_not_found_integration():
    """Інтеграційний тест: спроба отримати нотатку, якої немає (404 Error)."""
    # Робимо запит за ID, якого немає в базі
    response = client.get("/notes/999")

    # Перевіряємо, чи повернув сервер статус 404 (Not Found)
    assert response.status_code == 404
    assert response.json()["detail"] == "Нотатку не знайдено"
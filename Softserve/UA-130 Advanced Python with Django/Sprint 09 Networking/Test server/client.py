import requests
import json

BASE_URL = "http://localhost:8000"

# 1. Створюємо нового користувача
user = {
    "id": 5,
    "username": "client_user",
    "firstName": "Client",
    "lastName": "User",
    "email": "client@example.com",
    "password": "secure"
}
r = requests.post(f"{BASE_URL}/user", json=user)
print("POST status:", r.status_code, "| Response:", r.json())

# 2. Отримуємо всіх користувачів
r = requests.get(f"{BASE_URL}/users")
print("GET status:", r.status_code)
users = r.json()

# 3. Оновлюємо користувача
update = {
    "username": "updatedClient",
    "firstName": "Updated",
    "lastName": "User",
    "email": "updated@example.com",
    "password": "newpass"
}
r = requests.put(f"{BASE_URL}/user/5", json=update)
print("PUT status:", r.status_code, "| Response:", r.json())

# 4. Видаляємо користувача
r = requests.delete(f"{BASE_URL}/user/5")
print("DELETE status:", r.status_code, "| Response:", r.json())

# 5. Зберігаємо список користувачів у файл
with open("saved_users.txt", "w", encoding="utf-8") as file:
    file.write(json.dumps(users, indent=2, ensure_ascii=False))
print("✅ Дані збережено у файл: saved_users.txt")

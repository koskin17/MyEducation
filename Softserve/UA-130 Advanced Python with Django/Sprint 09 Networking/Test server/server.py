# 1. Підключається до **SQLite-бази даних**.
# 2. Зчитує з неї користувачів.
# 3. Обробляє запити `GET /users`, `POST /user`, `DELETE /user/<id>`.

## ✅ 📦 Підготовка
# Ми будемо використовувати:
# * `http.server` — для створення простого сервера
# * `sqlite3` — для роботи з базою
# * `json` — для обміну даними у форматі JSON
# Нічого додатково встановлювати не треба — все це вже є у стандартній бібліотеці Python.

## 🧩 Повний робочий код
import json
import sqlite3
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
    from pathlib import Path


# === 1. Створюємо або відкриваємо базу, створюємо таблицю ===
def init_db():
    db_path = Path(__file__).parent / "users.db"    # Get the current folder of python-script for save database

    # Create a database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            firstName TEXT,
            lastName TEXT,
            email TEXT,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()


# === 2. Клас сервера ===
class SimpleDBHandler(BaseHTTPRequestHandler):

    def _set_response(self, code=200, body=None):
        self.send_response(code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(body if body else {}).encode('utf-8'))

    def _parse_body(self):
        content_length = int(self.headers.get('Content-Length', 0))
        if content_length == 0:
            return None
        return json.loads(self.rfile.read(content_length).decode('utf-8'))

    def do_GET(self):
        """GET /users — повертає всіх користувачів з бази"""
        parsed = urlparse(self.path)

        if parsed.path == "/users":
            conn = sqlite3.connect("users.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users")
            rows = cursor.fetchall()
            conn.close()

            users = []
            for row in rows:
                users.append({
                    "id": row[0],
                    "username": row[1],
                    "firstName": row[2],
                    "lastName": row[3],
                    "email": row[4],
                    "password": row[5]
                })
            self._set_response(200, users)
        else:
            self._set_response(404, {"error": "Not found"})

    def do_POST(self):
        """POST /user — додає користувача до бази"""
        parsed = urlparse(self.path)

        if parsed.path == "/user":
            data = self._parse_body()
            if not data or "id" not in data or "username" not in data:
                self._set_response(400, {"error": "Invalid data"})
                return

            try:
                conn = sqlite3.connect("users.db")
                cursor = conn.cursor()
                cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)", (
                    data["id"],
                    data["username"],
                    data.get("firstName"),
                    data.get("lastName"),
                    data.get("email"),
                    data.get("password")
                ))
                conn.commit()
                conn.close()
                self._set_response(201, data)
            except sqlite3.IntegrityError:
                self._set_response(400, {"error": "User with this ID already exists"})
        else:
            self._set_response(404)

    def do_DELETE(self):
        """DELETE /user/<id> — видаляє користувача з бази"""
        parsed = urlparse(self.path)
        parts = parsed.path.strip("/").split("/")

        if len(parts) == 2 and parts[0] == "user":
            try:
                user_id = int(parts[1])
            except ValueError:
                self._set_response(400, {"error": "Invalid ID"})
                return

            conn = sqlite3.connect("users.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
            conn.commit()
            deleted = cursor.rowcount
            conn.close()

            if deleted:
                self._set_response(200, {})
            else:
                self._set_response(404, {"error": "User not found"})
        else:
            self._set_response(404, {"error": "Not found"})

    def do_PUT(self):
        """PUT /user/<id> — оновлює дані користувача"""
        parsed = urlparse(self.path)
        parts = parsed.path.strip("/").split("/")

        if len(parts) == 2 and parts[0] == "user":
            try:
                user_id = int(parts[1])
            except ValueError:
                self._set_response(400, {"error": "Invalid ID"})
                return

            data = self._parse_body()
            if not data or "username" not in data:
                self._set_response(400, {"error": "Invalid data"})
                return

            conn = sqlite3.connect("users.db")
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE users SET username = ?, firstName = ?, lastName = ?, email = ?, password = ?
                WHERE id = ?
            """, (
                data["username"],
                data.get("firstName"),
                data.get("lastName"),
                data.get("email"),
                data.get("password"),
                user_id
            ))
            conn.commit()
            updated = cursor.rowcount
            conn.close()

            if updated:
                self._set_response(200, {**data, "id": user_id})
            else:
                self._set_response(404, {"error": "User not found"})
        else:
            self._set_response(404, {"error": "Invalid path"})


# === 3. Запускаємо сервер ===
def run(host='localhost', port=8000):
    init_db()
    server_address = (host, port)
    httpd = HTTPServer(server_address, SimpleDBHandler)
    print(f"Сервер запущено: http://{host}:{port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run()


## 🧪 Як протестувати
# 1. 🔁 Запусти цей файл:
#    ```bash
#    python server_with_sqlite.py
#    ```
# 2. 🔎 Використовуй `requests` або Postman, щоб надіслати запити:
### GET:
# ```bash
# curl http://localhost:8000/users
# ```

### POST:
# ```bash
# curl -X POST http://localhost:8000/user -H "Content-Type: application/json" -d '{"id":1, "username":"admin", "firstName":"John", "lastName":"Smith", "email":"admin@example.com", "password":"1234"}'
# ```

### DELETE:
# ```bash
# curl -X DELETE http://localhost:8000/user/1
# ```


## ✅ Пояснення структури
# | Компонент                        | Призначення                                |
# | -------------------------------- | ------------------------------------------ |
# | `sqlite3.connect(...)`           | Підключення до локальної бази              |
# | `SELECT * FROM users`            | Отримати всі записи                        |
# | `INSERT INTO users VALUES (...)` | Додати користувача                         |
# | `DELETE FROM users WHERE id = ?` | Видалити користувача                       |
# | `BaseHTTPRequestHandler`         | Базовий клас сервера                       |
# | `urlparse(self.path)`            | Отримати шлях запиту (`/users`, `/user/1`) |

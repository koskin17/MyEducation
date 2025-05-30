import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse

# Глобальний список користувачів
USERS_LIST = [
    {
        "id": 1,
        "username": "theUser",
        "firstName": "John",
        "lastName": "James",
        "email": "john@email.com",
        "password": "12345",
    }
]

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def _set_response(self, status_code=200, body=None):
        """Sets an HTTP response with the given status and body."""
        
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(body if body else {}).encode('utf-8'))
        ## ✅ **2. Як працює `_set_response`**
        # # Це **не вбудований метод!** Це **наш власний** метод, який ми написали, щоб не дублювати однаковий код кожного разу.

        # ### Що він робить:
        # # * `self.send_response(status_code)` — встановлює код відповіді (наприклад, `200`, `404`, `400`).
        # # * `self.send_header('Content-type', 'application/json')` — каже браузеру, що ми відправляємо JSON.
        # # * `self.end_headers()` — завершує заголовки.
        # # * `self.wfile.write(...)` — надсилає тіло відповіді клієнту у форматі байтів.

        # ### 🔍 Приклад:
        # self._set_response(200, {"message": "OK"})
        # # Відповідь:
        # # * Status: 200 OK
        # # * Content-Type: application/json
        # # * Body: `{"message": "OK"}`

    def _pars_body(self):
        """Reads and parses the JSON body of the request."""

        content_length = int(self.headers.get('Content-Length', 0))
        ## ✅ **3. Що означає:**
        # content_length = int(self.headers.get('Content-Length', 0))
        ### 🔍 Пояснення:
        # * `self.headers` — це словник з HTTP-заголовками запиту (headers, які приходять від браузера/клієнта).
        # * `.get('Content-Length', 0)` — бере значення заголовка `"Content-Length"` (розмір тіла запиту в байтах), або `0`, якщо його нема.
        # * `int(...)` — перетворює значення у ціле число.

        ### 🔍 Приклад:
        # POST /user HTTP/1.1
        # Content-Length: 102
        # Content-Type: application/json

        # {"id": 1, "username": "theUser", ...}

        # → `Content-Length` буде `102`, і цей розмір використовується, щоб правильно зчитати тіло.

        if content_length == 0:
            return None
        try:
            return json.loads(self.rfile.read(content_length).decode('utf-8'))
            ### 🔍 Пояснення:
            # * `self.rfile` — це **"вхідний потік"** — тобто дані, які прийшли в запиті (тіло).
            # * `.read(content_length)` — читає точно `content_length` байтів.
            # * `.decode('utf-8')` — перетворює байти у текст.
            # * `json.loads(...)` — розбирає цей текст як JSON → повертає словник або список.

            ### 🔍 Приклад:
            # У запиті прийшло:
            # b'{"id": 1, "username": "admin"}'

            # Після read + decode:
            # '{"id": 1, "username": "admin"}'

            # Після json.loads:
            # {"id": 1, "username": "admin"}  ← dict
        except json.JSONDecodeError:
            return None
        
    def _is_valid_user(self, user):
        """Checks if the user object has all required fields."""

        required_fields = {"id", "username", "firstName", "lastName", "email", "password"}
        return isinstance(user, dict) and required_fields.issubset(user.keys())
        ## ✅ **1. Що означає:**
        # required_fields = {"username", "firstName", "lastName", "email", "password"}
        # return isinstance(data, dict) and required_fields.issubset(data.keys())

        ### 🔍 Пояснення:
        # * `required_fields` — це **множина** (set), в якій перераховані всі **обов’язкові поля** для користувача.
        # * `user` — це те, що прийшло від клієнта (наприклад, тіло POST-запиту у форматі JSON).
        # * `isinstance(user, dict)` — перевіряє, що `data` — це саме **словник (dict)**.
        # * `user.keys()` — повертає всі ключі у словнику `user`.
        # * `required_fields.issubset(data.keys())` — перевіряє, чи **всі обов'язкові поля є в словнику**.

        ### 🔍 Приклад 1 — вірний:
        # data = {
        #   "username": "test",
        #   "firstName": "John",
        #   "lastName": "Doe",
        #   "email": "john@email.com",
        #   "password": "123"
        # }
        # ✅ Всі потрібні поля є → `issubset` поверне `True`.

        ### 🔍 Приклад 2 — не вірний:
        # data = {
        #   "firstName": "John",
        #   "email": "john@email.com"
        # }
        # ⛔️ Відсутні `"username"`, `"lastName"` і `"password"` → `issubset` поверне `False`.
    
    def _is_valid_update_data(self, data):
        """Checks if the update object has all required fields."""

        required_fields = {"username", "firstName", "lastName", "email", "password"}
        return isinstance(data, dict) and required_fields.issubset(data.keys())

    def do_GET(self):
        parsed_path = urlparse(self.path)
        # ## **Як працює `urlparse`?**
        # ### 🔧 `urlparse(url)` — це функція, яка розбиває повний URL на складові частини:
        # Наприклад, якщо у тебе є такий URL:
        # from urllib.parse import urlparse

        # result = urlparse("http://localhost:8000/user/theUser?x=1#section")

        # Тоді `result` міститиме:
        # | Поле       | Значення           |
        # | ---------- | ------------------ |
        # | `scheme`   | `"http"`           |
        # | `netloc`   | `"localhost:8000"` |
        # | `path`     | `"/user/theUser"`  |
        # | `params`   | `""`               |
        # | `query`    | `"x=1"`            |
        # | `fragment` | `"section"`        |
        # Тобто `urlparse` розуміє структуру URL:
        # scheme://netloc/path;params?query#fragment
        # Ми у своєму випадку працюємо **в основному з `path`** — саме він містить те, що нам потрібно (`/reset`, `/users`, `/user/theUser` тощо).

        # urlparse(url)` **автоматично** знає, як правильно розбивати URL на частини
        # Він слідує **офіційній структурі URL**, описаній у [RFC 3986](https://www.rfc-editor.org/rfc/rfc3986):
        ### Структура URL за стандартом:
        # ```
        # scheme://netloc/path;params?query#fragment
        # ```
        ### Приклад:
        # from urllib.parse import urlparse

        # url = "https://example.com:8080/user/theUser?sort=name#top"
        # result = urlparse(url)

        # Отримаєш:
        # | Поле     | Значення           |
        # | -------- | ------------------ |
        # | scheme   | "https"            |
        # | netloc   | "example.com:8080" |
        # | path     | "/user/theUser"    |
        # | params   | ""                 |
        # | query    | "sort=name"        |
        # | fragment | "top"              |

        ### 📌 Що означає це на практиці:
        # * **scheme** — це протокол: `http`, `https`, `ftp` тощо
        # * **netloc** — хост + порт (наприклад, `localhost:8000`)
        # * **path** — шлях, який ми найчастіше використовуємо (`/reset`, `/user/...`)
        # * **query** — частина після `?`, наприклад: `?page=2`
        # * **fragment** — частина після `#`, зазвичай використовується в браузерах

        ### 🧩 Чи можна змінити "вшиту" структуру?
        # **Ні**, саму структуру `urlparse` змінити не можна, бо вона слідує міжнародному стандарту URL.
        # Але ти можеш **керувати тим, що туди передаєш**.
        # Наприклад:
        # urlparse("/user/theUser")  # працює як очікується, хоча це "відносний URL"
        # Тобто, навіть якщо немає `http://...`, `urlparse` все одно розуміє, що це — `path`.
        ## ✅ 2. Чому порівнюємо `len(path_parts) == 2`?
        # path_parts = parsed_path.path.strip("/").split("/")

        ### Наприклад:
        # URL: /user/theUser
        # parsed_path.path → "/user/theUser"
        # path_parts → ["user", "theUser"]

        # Отже:
        # len(path_parts) == 2
        # path_parts[0] == "user"
        # path_parts[1] == "theUser"

        ### ❓Навіщо порівнювати з 2?
        # Ми хочемо переконатися, що **шлях має саме два рівні**, наприклад:

        # | Шлях                    | path\_parts                      | Підходить? |
        # | ----------------------- | -------------------------------- | ---------- |
        # | `/user/theUser`         | `["user", "theUser"]`            | ✅          |
        # | `/user`                 | `["user"]`                       | ❌          |
        # | `/user/theUser/details` | `["user", "theUser", "details"]` | ❌          |

        # Тільки якщо **рівно два елементи**, ми знаємо:
        # * перший — це `"user"` (маршрут)
        # * другий — це `username` (параметр)

        # Тому ми і пишемо:
        # elif len(path_parts) == 2 and path_parts[0] == "user":

        ## ✨ Підсумок:
        # | Питання                           | Відповідь                                                            |
        # | --------------------------------- | -------------------------------------------------------------------- |
        # | `urlparse()` має вшиту структуру? | ✅ Так, вона стандартна: `scheme://netloc/path;params?query#fragment` |
        # | Можна змінити цю структуру?       | ❌ Ні, бо вона йде за стандартом RFC 3986                             |
        # | Навіщо `len(path_parts) == 2`?    | Щоб впевнитися, що шлях має дві частини: `/user/Ім'я`                |

        ## ✅ **5. Приклад використання `urlparse(self.path)`**
        # from urllib.parse import urlparse

        # parsed_path = urlparse("/user/theUser?sort=asc#top")

        # ### 🔍 Що буде в `parsed_path`?
        # Це **об'єкт `ParseResult`**:
        # ParseResult(
        #     scheme='', 
        #     netloc='', 
        #     path='/user/theUser', 
        #     params='', 
        #     query='sort=asc', 
        #     fragment='top'
        # )

        path_parts = parsed_path.path.strip("/").split("/")  # розбиваємо шлях на частини
        # ## **Навіщо `.strip("/")` перед `.split("/")`?**
        # Це потрібно для того, щоб правильно обробити шлях.
        # Подивись на приклад:
        # ```python
        # "/user/theUser".strip("/").split("/") → ["user", "theUser"]
        # ```
        # **Пояснення:**
        # * `strip("/")` прибирає `/` спочатку та в кінці, щоб не вийшов порожній елемент у списку.
        # * `.split("/")` ділить рядок по символу `/`.

        # 🔍 Без `strip("/")` ми отримаємо:
        # ```python
        # "/user/theUser".split("/") → ["", "user", "theUser"]
        # ```
        # І це незручно: перший елемент — порожній рядок.

        if parsed_path.path == "/reset":
            # ## **Як у `parsed_path.path` може з’явитись `/reset` або `/users`?**
            # Коли браузер або клієнт надсилає запит на адресу сервера, наприклад:
            # ```
            # http://localhost:8000/reset
            # ```
            # тоді у серверному коді в методі `do_GET(self)` буде:
            # ```python
            # self.path == "/reset"
            # ```
            # Ти можеш вивести це для перевірки:
            # ```python
            # print("Path:", self.path)
            # ```
            # Після `urlparse(self.path)`, у `parsed_path.path` буде тільки частина шляху, тобто `/reset`.
            
            # Якщо шлях точно `/reset`:
            # * Повертаємо список користувачів у початковий стан
            # * Відправляємо відповідь 200 OK
            # * Це означає, що ми скидаємо список користувачів до початкового стану

            global USERS_LIST
            USERS_LIST = [
                {
                    "id": 1,
                    "username": "theUser",
                    "firstName": "John",
                    "lastName": "James",
                    "email": "john@email.com",
                    "password": "12345",
                }
            ]
            self._set_response(200, USERS_LIST)

        elif parsed_path.path == "/users":
            # Якщо шлях `/users` — повертаємо весь список користувачів
            # ".path" означает только то, что мы берём поле с именем "path", которое доступно в перевенной "parsed_path".
            # В parsed_path будет объект с полями:
            # * `.scheme`
            # * `.netloc`
            # * `.path`
            # * `.params`
            # * `.query`
            # * `.fragment`

            # И `.path` — это просто название поля объекта, а не метод.
            # Пример:
            # self.path → "/user/theUser?sort=asc" - переданный путь
            # parsed_path = urlparse(self.path) - получили часть адреса "path"
            # parsed_path.path → "/user/theUser" - в результате при вызове мы получим вот такой результат.
            self._set_response(200, USERS_LIST)

        elif len(path_parts) == 2 and path_parts[0] == "user":
            username = path_parts[1]
            # Якщо шлях у вигляді `/user/ім’я`:
            # * Перевіряємо, чи є саме 2 частини — `["user", "theUser"]`
            # * Витягуємо ім’я користувача з другої частини
            user = next((user for user in USERS_LIST if user["username"] == username), None)
            # Шукаємо користувача у списку по `username`.
            # `next(...)` повертає першого знайденого, або `None`.
            #  функиция next() работает намного быстрее, чем обычный цикл for и она сразу останавливается, как только находит первого пользователя. Если использовать какой-то вариант с any(), то функция any() вернёт булевое значение True / False, а не имя пользователя, которое мы ищем.
            if user:
            # Якщо користувач знайдений — повертаємо його, інакше — помилка 400
                self._set_response(200, user)
            else:
                self._set_response(400, {"error": "User not found"})
        else:
            self._set_response(418)

    def do_POST(self):
        """Обробляє POST-запити:
        - /user — додає одного користувача
        - /user/createWithList — додає список користувачів
        """
        parsed_path = urlparse(self.path)
        # path_parts = parsed_path.path.strip("/").split("/")

        data = self._pars_body()
        if data is None:
            self._set_response(400, {})
            return

        global USERS_LIST

        if parsed_path.path == "/user":
            # Додавання одного користувача
            if not self._is_valid_user(data):
                self._set_response(400, {})
                return
            if any(u["id"] == data["id"] for u in USERS_LIST):
                self._set_response(400, {})
                return
            USERS_LIST.append(data)
            self._set_response(201, data)

        elif parsed_path.path == "/user/createWithList":
            # Додавання списку користувачів
            if not isinstance(data, list) or not all(self._is_valid_user(u) for u in data):
                self._set_response(400, {})
                return
            existing_ids = {u["id"] for u in USERS_LIST}
            new_ids = {u["id"] for u in data}
            if existing_ids & new_ids:
                self._set_response(400, {})
                return
            # > **Чому ми не пишемо `return self._set_response(400, {})`, а просто викликаємо `self._set_response(400, {})` і потім `return`?**

            # ## ✅ Коротка відповідь:
            # 🔸 Ми не пишемо `return self._set_response(...)`, бо **метод `_set_response()` нічого не повертає** (він повертає `None`).
            # 🔸 Тому ми викликаємо `_set_response(...)`, **щоб відправити відповідь клієнту**,
            # а потім просто робимо `return`, щоб **зупинити виконання функції `do_POST()`**.
            # ---
            # ## 🧩 Давайте розберемо на прикладі
            # ### Приклад:
            # ```python
            # def do_POST(self):
            #     data = self._pars_body()
            #     if data is None:
            #         self._set_response(400, {})
            #         return
            # ```
            # ### Детально:
            # * 🔹 `self._set_response(400, {})` — формує HTTP-відповідь з кодом 400 і пустим JSON.
            # * 🔹 `return` — зупиняє виконання `do_POST`.
            # ---
            # ### ❌ Що було б, якби написали:
            # ```python
            # return self._set_response(400, {})
            # ```
            # * Це теж спрацює, **але немає сенсу повертати `None`**, бо клієнту це не потрібно.
            # * Більше того, Python поверне `None` з `do_POST`, але `BaseHTTPRequestHandler` цього не чекає.
            # * Це може викликати **зайву плутанину** — ніби `self._set_response(...)` щось важливе повертає, хоча насправді ні.
            # ---
            # ## ✅ Тому правильний шаблон:
            # ```python
            # self._set_response(400, {"error": "Invalid data"})
            # return
            # ```
            # ---
            # ## 🧠 Пояснення на прикладі звичайної функції:
            # ```python
            # def print_and_return():
            #     print("Hello")
            #     return
            # print(print_and_return())  # Виведе: Hello, потім None
            # ```
            # Те саме відбувається з `_set_response()`:
            # * Він щось робить (виводить/відправляє), але **не повертає результат** → тобі немає чого повертати.
            # ---
            # ## ✅ Підсумок:
            # | Що                                        | Чому так                                                 |
            # | ------------------------------------------| -------------------------------------------------------- |
            # | `self._set_response(...)`                 | Формує відповідь, але **нічого не повертає**             |
            # | `return` після нього                      | Просто зупиняє виконання функції                         |
            # | Не треба писати
            # `return self._set_response(...)`            | Бо це лише збиває з пантелику — метод нічого не повертає |

            USERS_LIST.extend(data)
            self._set_response(201, data)
        else:
            self._set_response(418)

    def do_PUT(self):
        """Processes PUT requests:
            - /user/<id> — updates user data
        """

        parsed_path = urlparse(self.path)
        path_parts = parsed_path.path.strip("/").split("/")

        if len(path_parts) == 2 and path_parts[0] == "user":
            try:
                user_id = int(path_parts[1])
            except ValueError:
                self._set_response(404, {"error": "User not found"})
                return

            data = self._pars_body()
            if not self._is_valid_update_data(data):
                self._set_response(400, {"error": "not valid request data"})
                return

            global USERS_LIST
            for user in USERS_LIST:
                if user["id"] == user_id:
                    user.update(data)
                    self._set_response(200, user)
                    return
            self._set_response(404, {"error": "User not found"})
        else:
            self._set_response(418)

    def do_DELETE(self):
        """Обробляє DELETE-запити:
        - /user/<id> — видаляє користувача за ID
        """
        parsed_path = urlparse(self.path)
        path_parts = parsed_path.path.strip("/").split("/")

        if len(path_parts) == 2 and path_parts[0] == "user":
            try:
                user_id = int(path_parts[1])
            except ValueError:
                self._set_response(404, {"error": "User not found"})
                return

            global USERS_LIST
            for i, user in enumerate(USERS_LIST):
                if user["id"] == user_id:
                    USERS_LIST.pop(i)
                    self._set_response(200, {})
                    return
            self._set_response(404, {"error": "User not found"})
        else:
            self._set_response(418)


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, host='localhost', port=8000):
    server_address = (host, port)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()


if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()

## ✅ Пояснення реалізації
# * **`_set_response`**: Універсальний метод для встановлення статусу відповіді та відправлення JSON-тіла.
# * **`_parse_body`**: Зчитує та парсить JSON-тіло запиту. Повертає `None`, якщо тіло порожнє або некоректне.
# * **`_is_valid_user` та `_is_valid_update_data`**: Перевіряють, чи об'єкти мають всі необхідні поля для створення або оновлення користувача.
# * **`do_GET`**: Обробляє запити на `/reset`, `/users` та `/user/<username>`.
# * **`do_POST`**: Обробляє створення одного користувача (`/user`) або списку користувачів (`/user/createWithList`). Перевіряє наявність необхідних полів та унікальність `id`.
# * **`do_PUT`**: Оновлює дані користувача за `id`. Перевіряє валідність даних та наявність користувача.
# * **`do_DELETE`**: Видаляє користувача за `id`. Якщо користувача не знайдено, повертає помилку.

# ## 🧪 Рекомендації для тестування
# * Переконайся, що сервер запущено на порту, який використовують тести (наприклад, `8765`).
# * Перед кожним тестом виконуй запит на `/reset`, щоб повернути список користувачів до початкового стану.
# * Використовуй надані тести для перевірки коректності реалізації.

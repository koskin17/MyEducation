# 🎯 Objective:
# Implement a simplified Bank Account Management System in Python with the following key requirements:

# Use custom exceptions for input validation.

# Employ Python's logging module to log actions at both the application and per-account levels.

# ✅ Requirements:
# Create a custom exception class AccountError:
# Used to handle invalid account operations such as incorrect name type, negative balances, or invalid deposit/withdrawal amounts.
# Should automatically log the error message to a shared application log file.
# Define an Account class with the following features:
# Attributes:

# pk: unique ID for each account (auto-incremented).
# name: account holder’s name (string only).
# balance: starting from a non-negative number (int or float).

# Methods:
# deposit(amount): adds funds to the account (must be positive number).
# withdraw(amount): removes funds from the account (must be positive and ≤ balance).
# get_balance(): returns the current balance.
# __str__(): returns a string representation of the account.

# Logging:
# Global logging setup (app.log) with a basic configuration.
# Each account has a separate log file named account_<pk>.log.
# Log key actions: account creation, deposits, withdrawals, balance checks, and exceptions.

# Helper Function:
# Implement create_account(name, initial_balance) to handle account creation and exception logging gracefully.

# 📂 Deliverables:
# A single Python script containing:
# Class definitions
# Logging setup
# Log files should be generated automatically when operations are performed.

#### **Цель:**
# Реализовать **упрощённую систему управления банковскими счетами** на Python с учётом следующих требований:

### **Основные требования:**  
# ✅ Использовать **пользовательские исключения** для проверки входных данных.  
# ✅ Применять **модуль логирования** (`logging`) для регистрации действий как на уровне приложения, так и для каждого аккаунта.  

### **Что необходимо сделать?**  
### **1. Создать класс исключения `AccountError`**  
# - Используется для обработки **некорректных операций**, таких как:
#   - Неверный тип имени (должен быть `string`).
#   - Отрицательный баланс.
#   - Неверные суммы **депозита** или **снятия**.  
# - Ошибки должны **автоматически логироваться** в общем файле `app.log`.

### **2. Создать класс `Account`**  
# **Атрибуты:**  
# - `pk` → **уникальный идентификатор** счета (**авто-инкремент**).  
# - `name` → имя владельца счета (**только строка**).  
# - `balance` → начальный баланс (**не может быть отрицательным, `int` или `float`**).  

# **Методы:**  
# - `deposit(amount)` → **пополнение** счёта (**только положительное число**).  
# - `withdraw(amount)` → **снятие** денег (**только положительное число, не превышающее баланс**).  
# - `get_balance()` → **возвращает текущий баланс**.  
# - `__str__()` → **возвращает строковое представление счета**.  

### **3. Логирование (`logging`)**
# - **Общий лог-файл `app.log`** → хранит события всего приложения.  
# - **Лог-файл для каждого аккаунта** → `account_<pk>.log`.  
# - Логировать **основные события**:
#   - Создание счёта.
#   - Депозит.
#   - Снятие средств.
#   - Проверка баланса.
#   - Обработка ошибок.

### **4. Вспомогательная функция `create_account(name, initial_balance)`**  
# - **Обрабатывает исключения** и логирует их корректно.  
# - Создаёт новый аккаунт **с именем и начальным балансом**.  

### **Особый нюанс**
# 💡 **Авто-инкремент `pk` для каждого аккаунта** — это ключевой момент, который нужно учесть. Значение `pk` должно **увеличиваться** при каждом создании нового счёта.

# import logging

# # Настройка общего логирования
# logging.basicConfig(
#     filename="app.log",
#     filemode="w",
#     format="%(levelname)s: %(message)s",
#     level=logging.DEBUG
# )

# class AccountError(Exception):
#     """Пользовательское исключение для некорректных операций."""
#     def __init__(self, message):
#         super().__init__(message)
#         logging.error(message)  # Логируем ошибку в общем лог-файле


# class Account:
#     """Класс банковского счёта."""
#     account_counter = 1  # Авто-инкремент pk

#     def __init__(self, name, balance):
#         # Проверка типа name
#         if not isinstance(name, str):
#             raise AccountError("Invalid name type. Name must be a string.")

#         # Проверка начального баланса
#         if not isinstance(balance, (int, float)) or balance < 0:
#             raise AccountError("Invalid balance. Balance must be a non-negative number.")

#         # Уникальный идентификатор аккаунта (auto-increment)
#         self.pk = Account.account_counter
#         Account.account_counter += 1
#         self.name = name
#         self.balance = balance

#         # Настройка логирования для конкретного аккаунта
#         self.logger = logging.getLogger(f"Account_{self.pk}")
#         handler = logging.FileHandler(f"account_{self.pk}.log", mode="w")
#         formatter = logging.Formatter("%(levelname)s: %(message)s")
#         handler.setFormatter(formatter)
#         self.logger.addHandler(handler)

#         self.logger.info(f"Account {self.pk} created for {self.name} with balance {self.balance}")

#     def deposit(self, amount):
#         """Метод для пополнения счета."""
#         if not isinstance(amount, (int, float)) or amount <= 0:
#             raise AccountError("Invalid deposit amount. Must be a positive number.")

#         self.balance += amount
#         self.logger.info(f"Deposited {amount}. New balance: {self.balance}")

#     def withdraw(self, amount):
#         """Метод для снятия средств."""
#         if not isinstance(amount, (int, float)) or amount <= 0:
#             raise AccountError("Invalid withdrawal amount. Must be a positive number.")

#         if amount > self.balance:
#             raise AccountError("Insufficient funds for withdrawal.")

#         self.balance -= amount
#         self.logger.info(f"Withdrawn {amount}. New balance: {self.balance}")

#     def get_balance(self):
#         """Метод для проверки баланса."""
#         self.logger.info(f"Balance check. Current balance: {self.balance}")
#         return self.balance

#     def __str__(self):
#         return f"Account {self.pk}: {self.name}, Balance: {self.balance}"


# def create_account(name, initial_balance):
#     """Функция для создания аккаунта с обработкой ошибок."""
#     try:
#         account = Account(name, initial_balance)
#         return account
#     except AccountError as e:
#         logging.error(f"Failed to create account: {e}")
#         return None


# # Тестирование
# acc1 = create_account("Alice", 1000)
# acc2 = create_account(1234, 500)  # Ошибка: имя не строка
# acc3 = create_account("Bob", -200)  # Ошибка: отрицательный баланс

# if acc1:
#     acc1.deposit(500)  # Депозит 500
#     acc1.withdraw(200)  # Снятие 200
#     acc1.get_balance()  # Проверка баланса

### **Объяснение кода**
# ✔ **Класс `AccountError`** — для обработки ошибок, автоматически логирует их в `app.log`.  
# ✔ **Класс `Account`** — представляет банковский счёт и содержит:
#    - Авто-инкремент `pk` (`account_counter`).
#    - Логирование каждого счета (`account_<pk>.log`).
# ✔ **Методы (`deposit`, `withdraw`, `get_balance`)**:
#    - Проверяют **правильность данных**.
#    - Логируют **каждое действие**.
# ✔ **Функция `create_account(name, initial_balance)`**:
#    - Обрабатывает **ошибки** при создании счета.
#    - Логирует **успешные и неудачные попытки**.

# 🔹 **Вывод**  
# Этот код соответствует всем требованиям задачи:
# ✅ Пользовательские исключения `AccountError`.  
# ✅ Логирование **на уровне приложения и аккаунта** (`app.log`, `account_<pk>.log`).  
# ✅ Авто-инкремент `pk`.  
# ✅ Корректная обработка ошибок.

# Твоє рішення дуже добре — чітке, чисте і грамотно побудоване. Але як досвідчений Python-розробник я можу дати як позитивну оцінку, так і деякі **точкові поради для покращення**.

# ---

# ## ✅ Що зроблено **відмінно**:

# | Компонент                                       | Оцінка                                                    |
# | ----------------------------------------------- | --------------------------------------------------------- |
# | **Кастомне виключення `AccountError`**          | ✔ Відповідає вимогам, логування через `logging.error()` ✅ |
# | **Клас `Account` з автоінкрементом pk**         | ✔ Чітка інкапсуляція, унікальний `pk`, збереження стану   |
# | **Логування в окремі файли `account_<pk>.log`** | ✔ Ідеально! Відповідає техзавданню                        |
# | **Методи `deposit`, `withdraw`, `get_balance`** | ✔ Валідність + логування ✅                                |
# | **Функція `create_account(...)`**               | ✔ Винесена логіка створення + захист через try-except ✅   |
# | **Форматування, структура, читабельність**      | ✔ Дуже чисто, читається легко                             |

# ---

# ## 🛠 Що можна покращити

# ### 1. 🧹 Логгер кожного аккаунта створює **новий обробник (`handler`) при кожному виклику**

# Це призведе до **дублювання логів**, якщо об'єкт створюється декілька разів (наприклад, при десеріалізації).
# 🔧 **Рішення** — перевіряти, чи вже додано обробник:

# ```python
# if not self.logger.handlers:
#     handler = logging.FileHandler(f"account_{self.pk}.log", mode="w")
#     ...
#     self.logger.addHandler(handler)
# ```

# ---

# ### 2. ⚠ Логгер `AccountError` — це не власний логгер, а глобальний `root`

# > Це не помилка, але краще зробити **спеціальний `app_logger`** для загального логування.

# ```python
# app_logger = logging.getLogger("app")
# app_logger.setLevel(logging.DEBUG)
# app_handler = logging.FileHandler("app.log", mode="w")
# app_handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
# app_logger.addHandler(app_handler)
# ```

# І використовувати `app_logger.error(...)` замість `logging.error(...)`.

# ---

# ### 3. 🧪 Метод `get_balance()` логічно не повинен логувати кожен запит

# Лог кожного виклику балансу швидко «заб’є» лог-файл, особливо при інтерактивному доступі.
# 📌 Пропозиція: або прибрати логування звідти, або робити його на DEBUG-рівні:

# ```python
# self.logger.debug(f"Balance check. Current balance: {self.balance}")
# ```

# ---

# ### 4. 🧼 Метод `__str__()` — краще привести баланс до двох знаків:

# ```python
# return f"Account {self.pk}: {self.name}, Balance: {self.balance:.2f}"
# ```

# ---

# ### 5. 🚀 Додати `__repr__()` — для зручної інтерактивної роботи (не обов'язково)

# ```python
# def __repr__(self):
#     return f"Account(pk={self.pk}, name='{self.name}', balance={self.balance})"
# ```

# ---

# ## 💯 Загальна оцінка:

# * **Реалізація**: ✅ 9.5 / 10
# * **Стабільність**: ✅ Надійна
# * **Логіка**: ✅ Відповідає ТЗ
# * **Можливість масштабування**: 🔧 Потрібна обережність з logger'ами


# Ось повна версія покращеного рішення, яке:
# * ✅ використовує розділені логери (`app_logger` і логер для кожного акаунта),
# * ✅ захищає від дублювання обробників,
# * ✅ додає формат балансу з двома знаками,
# * ✅ не перевантажує лог при виклику `get_balance()` (DEBUG-рівень),
# * ✅ містить `__repr__()` для зручності відладки.

## 🔧 Повний код:
import logging

# 🔹 Глобальний логгер додатку
app_logger = logging.getLogger("app")
app_logger.setLevel(logging.DEBUG)

app_handler = logging.FileHandler("app.log", mode="w")
app_handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
app_logger.addHandler(app_handler)


class AccountError(Exception):
    """Пользовательское исключение для некорректных операций."""
    def __init__(self, message):
        super().__init__(message)
        app_logger.error(message)  # Записываем ошибку в лог приложения


class Account:
    """Класс банковского счёта."""
    account_counter = 1  # Авто-инкремент pk

    def __init__(self, name, balance):
        # Валидация имени
        if not isinstance(name, str):
            raise AccountError("Invalid name type. Name must be a string.")

        # Валидация баланса
        if not isinstance(balance, (int, float)) or balance < 0:
            raise AccountError("Invalid balance. Balance must be a non-negative number.")

        # Инициализация аккаунта
        self.pk = Account.account_counter
        Account.account_counter += 1
        self.name = name
        self.balance = balance

        # 🔹 Настройка индивидуального логгера
        self.logger = logging.getLogger(f"Account_{self.pk}")
        self.logger.setLevel(logging.DEBUG)

        if not self.logger.handlers:
            handler = logging.FileHandler(f"account_{self.pk}.log", mode="w")
            formatter = logging.Formatter("%(levelname)s: %(message)s")
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

        self.logger.info(f"Account {self.pk} created for {self.name} with balance {self.balance:.2f}")

    def deposit(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise AccountError("Invalid deposit amount. Must be a positive number.")

        self.balance += amount
        self.logger.info(f"Deposited {amount:.2f}. New balance: {self.balance:.2f}")

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise AccountError("Invalid withdrawal amount. Must be a positive number.")

        if amount > self.balance:
            raise AccountError("Insufficient funds for withdrawal.")

        self.balance -= amount
        self.logger.info(f"Withdrawn {amount:.2f}. New balance: {self.balance:.2f}")

    def get_balance(self):
        self.logger.debug(f"Balance check. Current balance: {self.balance:.2f}")
        return self.balance

    def __str__(self):
        return f"Account {self.pk}: {self.name}, Balance: {self.balance:.2f}"

    def __repr__(self):
        return f"Account(pk={self.pk}, name='{self.name}', balance={self.balance:.2f})"


def create_account(name, initial_balance):
    """Функция для создания аккаунта с обработкой ошибок."""
    try:
        account = Account(name, initial_balance)
        return account
    except AccountError as e:
        app_logger.error(f"Failed to create account: {e}")
        return None


# 🔸 Пример использования (можно удалить при импорте как модуля)
if __name__ == "__main__":
    acc1 = create_account("Alice", 1000)
    acc2 = create_account("Bob", -50)  # Ошибка
    if acc1:
        acc1.deposit(500)
        acc1.withdraw(200)
        print(acc1.get_balance())
        print(acc1)

# ## 🧪 Результат при запуску:

# * Створюється `app.log` з усіма загальними помилками.
# * Для кожного акаунта — окремий `account_<pk>.log`.
# * Програма стабільна, читаємість коду висока.

# ---

# Хочеш — можу також:

# * Додати логування дати та часу,
# * Зберігати акаунти у файл,
# * Зробити REST API для роботи з акаунтами.

# Пиши, якщо продовжимо 🙂


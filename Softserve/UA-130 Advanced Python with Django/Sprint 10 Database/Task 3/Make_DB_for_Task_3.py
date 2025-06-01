## 🛠️ **Скрипт для створення бази `q1.db` локально:**
import sqlite3
from pathlib import Path

def create_test_database():
    db_path = Path(__file__).parent / "q1.db"  # Get the current folder of python-script for save database

    # Create or connect to DB
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    # Delete table if it exists
    cursor.execute("DROP TABLE IF EXISTS customers")

    # Create a table customers
    cursor.execute("""
        CREATE TABLE customers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            city TEXT NOT NULL,
            grade INTEGER NOT NULL,
            salesperson_id INTEGER NOT NULL
        )
    """)

    # Add test data to table
    sample_data = [
        (3022, "Nik Rimando", "Madrid", 1000, 6001),
        (3025, "Grem Zusisa", "USA", 2000, 6002),
        (3001, "Brad Guzan", "London", 100, 5005),
        (3002, "Nick Rimando", "New York", 150, 5001),
        (3003, "Jozy Altidore", "Kyiv", 200, 5007),
        (3004, "Fabian Johns", "Paris", 300, 5006),
        (3005, "Graham Zusi", "California", 180, 5002),
        (3006, "Julian Green", "London", 400, 5001),
        (3007, "Geoff Cameron", "Berlin", 2590, 6003),
        (3008, "Brad Davis", "New York", 2400, 6004),
        (3009, "Tim Howard", "Chicago", 175, 6005),
        (3010, "Michael Bradley", "Toronto", 300, 6006),
        (3011, "Clint Dempsey", "Seattle", 210, 6007),
        (3012, "Landon Donovan", "Los Angeles", 190, 6008),
        (3013, "Benny Feilhaber", "Kansas City", 500, 6009),
        (3014, "Sacha Kljestan", "Orlando", 225, 6010),
        (3015, "Kyle Beckerman", "Salt Lake", 400, 6011),
        (3016, "Jermaine Jones", "Frankfurt", 330, 6012),
        (3017, "Matt Besler", "Texas", 199, 6013),
        (3018, "DeAndre Yedlin", "Newcastle", 410, 6014),
        (3019, "Omar Gonzalez", "Pachuca", 390, 6015),
        (3020, "Tim Ream", "London", 275, 6016),
        (3021, "Chris Wondolowski", "San Jose", 305, 6017),
        (3023, "Jozy Morris", "Toronto", 90, 6018),
        (3024, "Ale Bedoya", "Philadelphia", 215, 6019),
        (3026, "John Brooks", "Berlin", 220, 6020),
        (3027, "Zack Steffen", "Dusseldorf", 100, 6021),
        (3028, "Paul Arriola", "San Diego", 340, 6022)
    ]

    cursor.executemany("""
        INSERT INTO customers (id, name, city, grade, salesperson_id)
        VALUES (?, ?, ?, ?, ?)
    """, sample_data)

    # Save changes aтв close connestion
    connection.commit()
    connection.close()
    print("Database q1.db created with test data.")

# Start making Database
create_test_database()

## ✅ Що робити:
# 1. **Скопіюй цей код у Python-файл**, наприклад `create_q1_db.py`.
# 2. Запусти його **в тій самій папці**, де ти плануєш запускати основний скрипт (`fetch_customers_with_high_grades()`).
# 3. У результаті з'явиться файл **`q1.db`**, і твій скрипт для виводу клієнтів із `grade > 200` буде працювати з ним.

## 🧪 Очікуваний результат при запуску основного скрипта:
# Connected to SQLite
# Total rows are:   3
# Printing each row
# Id:  3004
# Name:  Fabian Johns
# City:  Paris
# Grade:  300
# Seller:  5006

# Id:  3022
# Name:  Nik Rimando
# City:  Madrid
# Grade:  1000
# Seller:  6001

# Id:  3025
# Name:  Grem Zusisa
# City:  USA
# Grade:  2000
# Seller:  6002

# The SQLite connection is closed

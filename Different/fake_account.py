# Модуль для получения фейковых данных людей
from faker import Faker


fake = Faker(locale="Ru-ru")
# Получение 10-ти фейковых имён
for _ in range(10):
    print(fake.name())

# Получение 10-ти фейковых адресов
for _ in range(10):
    print(fake.address())

# Получение 10-ти фейковых url-адресов и адресов почты
for _ in range(10):
    print(fake.url())
    print(fake.email())
# Всё вместе
for _ in range(10):
    print(fake.name(), fake.address(), fake.email())

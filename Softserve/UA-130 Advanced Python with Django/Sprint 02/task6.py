# Please specify a regular expression for matching publication formats such as "Head First. Python: PROSystem, 2021 and "Coding for Kids Python & Blockchain Programming: Elliot Davis, 2022

# For example:

# Тест	Result
# if 're' in sys.modules:
#     print(True)
# True
# data = '"Head First. Python: PROSystem, 2021"# and "Coding for Kids Python & Blockchain Programming: Elliot Davis, 2022"'

# for item in pretty_message(data):
#     print(item)
# ('Head First. Python', 'PROSystem', '2021')
# ('Coding for Kids Python & Blockchain Programming', 'Elliot Davis', '2022')

# Ты можешь использовать регулярное выражение для извлечения названия книги, автора (или издателя) и года из строки.  

### **Готовое регулярное выражение**
# Нужно изменить часть шаблона, отвечающую за название книги, чтобы она могла содержать двоеточия. Раньше использовалось ([^:]+), то есть «всё, что не является двоеточием», а это приводит к тому, что при наличии двоеточия в названии (как в последней записи) захватывается только часть до первого двоеточия. Решение – заменить эту группу на жадную (.+), которая захватывает всё (включая двоеточия) до разделителя, определяемого следующим регулярным выражением (то есть до разделителя перед автором и годом).
# Вот окончательный рабочий вариант:
import re

def pretty_message(data):
    pattern = r'"([^"]+):\s*([^,"]+),\s*(\d{4})"'
    return re.findall(pattern, data)


# Пробуем на тестовых данных:
data = '"Head First. Python: PROSystem, 2021"# and "Coding for Kids Python & Blockchain Programming: Elliot Davis, 2022"'

for item in pretty_message(data):
    print(item)

data = '"Head First. Python: PROSystem, 2021" "Coding for Kids Python & Blockchain Programming: Elliot Davis, 2022" "Data Science Essentials: John Smith, 2019" "Web Development Basics: Jane Doe, 2020"'
for item in pretty_message(data):
    print(item)

data = '"Design Patterns in Java: Gang of Four, 1994", "Introduction to Algorithms: Thomas H. Cormen, 2009" - "Clean Code: Robert C. Martin, 2008"; "The Pragmatic Programmer: Andrew Hunt, 1999" and "Artificial Intelligence: A Modern Approach: Stuart Russell, 2003"'
for item in pretty_message(data):
    print(item)

# Детальное объяснение
# - Начало и конец совпадения
# Выражение начинается с " и заканчивается на " – это гарантирует, что совпадение происходит только внутри парных кавычек.
# - Первая захватывающая группа – название книги
# Используется конструкция ([^"]+) – она означает «один и более символов, отличных от кавычки». Таким образом, даже если в названии книги есть двоеточия, они будут попадать в группу, но при этом символ " не входит в совпадение.
# После группы идёт литерал : и возможные пробельные символы (\s*).
# - Вторая захватывающая группа – имя автора
# Ауди применяется ([^,"]+) – означает «один и более символов, кроме запятой и кавычки». Таким образом, имя автора захватывается до запятой, которая отделяет автора от года.
# - Третья группа – год издания
# (\d{4}) – захватывает ровно четыре цифры, что соответствует году издания.
# Почему это решение работает правильно
# - Каждый фрагмент книги должен быть обрамлён двойными кавычками. Использование [^"]+ гарантирует, что содержимое внутри кавычек не "перетянется" на следующую книгу.
# - При наличии лишних двоеточий (например, в «Artificial Intelligence: A Modern Approach: Stuart Russell, 2003») группа ([^"]+) благодаря жадности захватывает максимально возможное количество символов, но при этом регулярное выражение корректно «откатывается» так, чтобы литерал : перед автором оказался именно тем разделителем, который позволяет далее сопоставить автора и год.
# При данных тестовых строках результат будет таким:

# ('Design Patterns in Java', 'Gang of Four', '1994')
# ('Introduction to Algorithms', 'Thomas H. Cormen', '2009')
# ('Clean Code', 'Robert C. Martin', '2008')
# ('The Pragmatic Programmer', 'Andrew Hunt', '1999')
# ('Artificial Intelligence: A Modern Approach', 'Stuart Russell', '2003')
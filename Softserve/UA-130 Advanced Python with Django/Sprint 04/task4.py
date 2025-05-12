# Your task is to write a program which allows teachers to create a multiple choice test in a class called Testpaper and to be also able to assign a minimum pass mark. The testpaper's subject should also be included. The attributes are in the following order:

# 1. subject
# 2. markscheme
# 3. pass_mark
# As well as that, we need to create student objects to take the test itself! Create another class called Student and do the following:

# Create an attribute called tests_taken and set the default as  'No tests taken'.
# Make a method called take_test(), which takes in the testpaper object they are completing and the student's answers. Compare what they wrote to the mark scheme, and append to the/create a dictionary assigned to tests_taken in the way as shown in the point below.
# Each key in the dictionary should be the testpaper subject and each value should be a string in the format seen in the examples below (whether or not the student has failed, and their percentage in brackets).
# Example:

# paper1 = Testpaper("Maths", ["1A", "2C", "3D", "4A", "5A"], "60%")
# paper2 = Testpaper("Chemistry", ["1C", "2C", "3D", "4A"], "75%")
# paper3 = Testpaper("Computing", ["1D", "2C", "3C", "4B", "5D", "6C", "7A"], "75%")

# student1 = Student()
# student2 = Student()
# student1.tests_taken ➞ "No tests taken"
# student1.take_test(paper1, ["1A", "2D", "3D", "4A", "5A"])
# student1.tests_taken ➞ {"Maths" : "Passed! (80%)"}

# student2.take_test(paper2, ["1C", "2D", "3A", "4C"])
# student2.take_test(paper3, ["1A", "2C", "3A", "4C", "5D", "6C", "7B"])
# student2.tests_taken ➞ {"Chemistry" : "Failed! (25%)", "Computing" : "Failed! (43%)"}

# Напишите программу, которая позволяет учителям создавать тесты с несколькими вариантами ответов в классе Testpaper и устанавливать минимальный проходной балл. Тест должен включать в себя:
# - subject – предмет теста
# - markscheme – правильные ответы
# - pass_mark – минимальный процент для прохождения
# Также необходимо создать класс Student, который может проходить тесты. Для этого:
# - Создайте атрибут tests_taken со значением "No tests taken" по умолчанию.
# - Реализуйте метод take_test(), который принимает тест Testpaper и список ответов студента, сравнивает ответы с правильными и добавляет результат в tests_taken.
# - tests_taken хранит словарь, где ключ – это предмет теста, а значение – строка с результатом (прошёл/не прошёл + процент правильных ответов).
# Примеры использования:
# paper1 = Testpaper("Maths", ["1A", "2C", "3D", "4A", "5A"], "60%")
# paper2 = Testpaper("Chemistry", ["1C", "2C", "3D", "4A"], "75%")
# paper3 = Testpaper("Computing", ["1D", "2C", "3C", "4B", "5D", "6C", "7A"], "75%")

# student1 = Student()
# student2 = Student()

# print(student1.tests_taken)  # "No tests taken"

# student1.take_test(paper1, ["1A", "2D", "3D", "4A", "5A"])
# print(student1.tests_taken)  # {"Maths" : "Passed! (80%)"}

# student2.take_test(paper2, ["1C", "2D", "3A", "4C"])
# student2.take_test(paper3, ["1A", "2C", "3A", "4C", "5D", "6C", "7B"])
# print(student2.tests_taken)  # {"Chemistry" : "Failed! (25%)", "Computing" : "Failed! (43%)"}

class Testpaper:
    def __init__(self, subject, markscheme, pass_mark):
        """Инициализация теста"""
        self.subject = subject               # Название предмета
        self.markscheme = markscheme          # Список правильных ответов
        self.pass_mark = int(pass_mark[:-1])  # Проходной процент (убираем '%' и превращаем в число)

class Student:
    def __init__(self):
        """Создание студента"""
        self.tests_taken = "No tests taken"  # По умолчанию: нет пройденных тестов

    def take_test(self, testpaper, answers):
        """Прохождение теста и сохранение результата"""
        # Подсчитываем количество правильных ответов
        correct_answers = sum(1 for a, b in zip(answers, testpaper.markscheme) if a == b)
        total_questions = len(testpaper.markscheme)  # Общее число вопросов
        percentage = (correct_answers / total_questions) * 100  # Вычисление процента

        # Определяем, прошёл ли студент тест
        result = "Passed!" if percentage >= testpaper.pass_mark else "Failed!"
        result += f" ({round(percentage)}%)"  # Округляем процент

        # Обновляем `tests_taken` (изменяем `"No tests taken"` на словарь)
        if self.tests_taken == "No tests taken":
            self.tests_taken = {}  
        self.tests_taken[testpaper.subject] = result

# Подробное, пошаговое объяснение кода
# 🔹 Класс Testpaper (экземпляр теста)
# - subject – название предмета.
# - markscheme – список правильных ответов (например, ["1A", "2C", "3D"]).
# - pass_mark – минимальный процент правильных ответов для прохождения ("60%" → 60).
# 🔹 Класс Student (экземпляр студента)
# - Атрибут tests_taken:
# - По умолчанию "No tests taken", если студент ещё не проходил тесты.
# - После первого теста tests_taken превращается в словарь вида {"Maths": "Passed! (80%)"}.
# - Метод take_test(testpaper, answers):
# - Принимает объект теста Testpaper и список ответов студента.
# - Сравнивает ответы студента с правильными (markscheme).
# - Подсчитывает процент правильных ответов.
# - Формирует строку "Passed! (XX%)" или "Failed! (XX%)", в зависимости от проходного балла.
# - Обновляет tests_taken.

# ✅ Проверим код на примерах
# # Создаем тесты
paper1 = Testpaper("Maths", ["1A", "2C", "3D", "4A", "5A"], "60%")
paper2 = Testpaper("Chemistry", ["1C", "2C", "3D", "4A"], "75%")
paper3 = Testpaper("Computing", ["1D", "2C", "3C", "4B", "5D", "6C", "7A"], "75%")

# # Создаем студентов
student1 = Student()
student2 = Student()

print(student1.tests_taken)  # "No tests taken"

# # Student 1 проходит тест по математике
student1.take_test(paper1, ["1A", "2D", "3D", "4A", "5A"])
print(student1.tests_taken)  # {"Maths" : "Passed! (80%)"}

# # Student 2 проходит тест по химии и по информатике
student2.take_test(paper2, ["1C", "2D", "3A", "4C"])
student2.take_test(paper3, ["1A", "2C", "3A", "4C", "5D", "6C", "7B"])
print(student2.tests_taken)  # {"Chemistry" : "Failed! (25%)", "Computing" : "Failed! (43%)"}


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

# class Testpaper:
#     def __init__(self, subject, markscheme, pass_mark):
#         """Test initialization"""
#         self.subject = subject               # subject name
#         self.markscheme = markscheme          # List of correct answers
#         self.pass_mark = int(pass_mark[:-1])  # Passing percentage (remove '%' and turn into a number)

# class Student:
#     def __init__(self):
#         """Creating a student"""
#         self.tests_taken = "No tests taken"  # Default: no passed tests

#     def take_test(self, testpaper, answers):
#         """Take the test and save the result"""
#         # Count the number of correct answers
#         correct_answers = sum(1 for a, b in zip(answers, testpaper.markscheme) if a == b)
#         total_questions = len(testpaper.markscheme)  # Total number of questions
#         percentage = (correct_answers / total_questions) * 100  # Calculating percentage

#         # Determine whether the student passed the test
#         result = "Passed!" if percentage >= testpaper.pass_mark else "Failed!"
#         result += f" ({round(percentage)}%)"  # Rounding off the percentage

#         # Update `tests_taken` (change `"No tests taken"` to a dictionary)
#         if self.tests_taken == "No tests taken":
#             self.tests_taken = {}  
#         self.tests_taken[testpaper.subject] = result

class Testpaper:
    def __init__(self, subject, markscheme, pass_mark):
        """Test initialization"""
        self.subject = subject              # subject name
        self.markscheme = markscheme       # List of correct answers
        self._pass_mark_value = int(pass_mark.strip().rstrip('%'))  # numerical values
        self._pass_mark_str = pass_mark.strip()                     # for display

    @property
    def pass_mark(self):
        """Returns the passing score as a string"""
        return self._pass_mark_str

    def get_pass_mark_value(self):
        """Returns a numeric value for comparison"""
        return self._pass_mark_value


class Student:
    def __init__(self):
        """Creating a student"""
        self.tests_taken = "No tests taken" # Default: no passed tests

    def take_test(self, testpaper, answers):
        """Take the test and save the result"""
        # Count the number of correct answers
        correct = sum(1 for a, b in zip(answers, testpaper.markscheme) if a == b)
        total = len(testpaper.markscheme)   # Total number of questions
        percentage = (correct / total) * 100    # Calculating percentage
        rounded_percentage = round(percentage)

        # Compare with a numeric value
        if rounded_percentage >= testpaper.get_pass_mark_value():
            result = f"Passed! ({rounded_percentage}%)"
        else:
            result = f"Failed! ({rounded_percentage}%)"

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
# paper1 = Testpaper("Maths", ["1A", "2C", "3D", "4A", "5A"], "60%")
# paper2 = Testpaper("Chemistry", ["1C", "2C", "3D", "4A"], "75%")
# paper3 = Testpaper("Computing", ["1D", "2C", "3C", "4B", "5D", "6C", "7A"], "75%")

# # # Создаем студентов
# student1 = Student()
# student2 = Student()

# print(student1.tests_taken)  # "No tests taken"

# # # Student 1 проходит тест по математике
# student1.take_test(paper1, ["1A", "2D", "3D", "4A", "5A"])
# print(student1.tests_taken)  # {"Maths" : "Passed! (80%)"}

# # # Student 2 проходит тест по химии и по информатике
# student2.take_test(paper2, ["1C", "2D", "3A", "4C"])
# student2.take_test(paper3, ["1A", "2C", "3A", "4C", "5D", "6C", "7B"])
# print(student2.tests_taken)  # {"Chemistry" : "Failed! (25%)", "Computing" : "Failed! (43%)"}

# Тест1
paper1 = Testpaper('Maths', ['1A', '2C', '3D', '4A', '5A'], '60%')
student1 = Student()
print(student1.tests_taken)
student1.take_test(paper1, ['1A', '2D', '3D', '4A', '5A'])
print(student1.tests_taken)
print(paper1.subject)
print(paper1.markscheme)
print(paper1.pass_mark)

# Тест2
paper2 = Testpaper('Chemistry', ['1C', '2C', '3D', '4A'], '75%')
student2 = Student()
student2.take_test(paper2, ['1C', '2D', '3A', '4C'])
print(student2.tests_taken)
print(paper2.subject)
print(paper2.markscheme)
print(paper2.pass_mark)

# Тест3
paper3 = Testpaper('Computing', ['1D', '2C', '3C', '4B', '5D', '6C', '7A'], '75%')
student2 = Student()
student3 = Student()
student2.take_test(paper3, ['1A', '2C', '3A', '4C', '5D', '6C', '7B'])
print(student3.tests_taken)
student3.take_test(paper1, ['1C', '2D', '3A', '4C', '5A'])
student3.take_test(paper3, ['1A', '2C', '3A', '4C', '5D', '6C', '7B'])
print(student3.tests_taken)
print(paper3.subject)
print(paper3.markscheme)
print(paper3.pass_mark)

# Тест4
student3 = Student()
paper4 = Testpaper('Physics', ['1A', '2B', '3A', '4C', '5A', '6C', '7A', '8C', '9D', '10A', '11A'], '90%')
student3.take_test(paper4, ['1A', '2C', '3A', '4C', '5D', '6C', '7B', '8C', '9D', '10A', '11A'])
print(student3.tests_taken)
print(paper4.subject)
print(paper4.markscheme)
print(paper4.pass_mark)
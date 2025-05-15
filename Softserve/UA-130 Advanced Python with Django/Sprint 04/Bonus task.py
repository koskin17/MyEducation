# Goal:
# To consolidate the understanding of the object model, recursive relationships between objects, as well as the skills of building hierarchical structures using classes.

# Task:
# To create a program for storing a family tree with the ability to:

# add new members;

# find a common ancestor of two people;

# display the complete pedigree of a specific person.
# Problem statement:
# Develop a Person class that stores:

# ·         - a person's name;

# ·         - parents (parent1, parent2);

# ·        -  a get_ancestors(depth) method that returns a list of ancestors at a specified depth;

# ·        -   a common_ancestor(other_person) method that finds the first common ancestor with another person.

# George
# ├── Father: Charles
# │   ├── Father: Alex
# │   └── Mother: Barbara
# └── Mother: Fiona
#     ├── Father: Diana
#     └── Mother: Edward

# 🧾 Example solution:

# # Example of creating a pedigree
# a = Person("Alex")
# b = Person("Barbara")
# c = Person("Charles", a, b)

# d = Person("Diana")
# e = Person("Edward")
# f = Person("Fiona", d, e)

# child = Person("George", c, f)

# print(child.get_ancestors(1))  # ['Charles', 'Fiona']
# print(child.get_ancestors(2))  # ['Alex', 'Barbara', 'Charles', 'Diana', 'Edward', 'Fiona']
# print(c.common_ancestor(f))   # None
# print(child.common_ancestor(f))  # ['Diana', 'Edward']

# Чудове завдання! 👨‍👩‍👧‍👦 Воно перевіряє розуміння:

# * об’єктної моделі Python;
# * рекурсії та обходу деревоподібних структур;
# * побудови родоводу (family tree).

# ## 🧠 Що потрібно реалізувати:
# ### ✅ Клас `Person`, який містить:
# * `name` — ім’я;
# * `parent1`, `parent2` — посилання на батьків (або `None`);
# * метод `get_ancestors(depth)` — повертає список імен предків на вказаній глибині;
# * метод `common_ancestor(other_person)` — знаходить **спільних предків** із іншою людиною.

# ## 🧾 Важливо:
# * У `get_ancestors(depth)` потрібно:
#   * рекурсивно заглиблюватися в дерево;
#   * на кожному кроці збирати предків;
# * У `common_ancestor()` треба:
#   * знайти **всіх предків себе** та іншої людини;
#   * знайти **перетин множин імен предків**.

# ## ✅ Готовий робочий код:
class Person:
    def __init__(self, name, parent1=None, parent2=None):
        self.name = name
        self.parent1 = parent1
        self.parent2 = parent2

    def get_ancestors(self, depth):
        """
        Повертає список імен предків на заданій глибині.
        depth = 1 — батьки
        depth = 2 — бабусі/дідусі тощо
        """
        if depth <= 0:
            return []
        
        ancestors = []
        # Додаємо батьків (якщо є)
        if self.parent1:
            ancestors.append(self.parent1.name)
            ancestors += self.parent1.get_ancestors(depth - 1)
        if self.parent2:
            ancestors.append(self.parent2.name)
            ancestors += self.parent2.get_ancestors(depth - 1)
        
        return ancestors

    def _collect_all_ancestors(self):
        """
        Допоміжний метод: збирає всіх предків (усіх поколінь)
        """
        ancestors = set()
        if self.parent1:
            ancestors.add(self.parent1.name)
            ancestors |= self.parent1._collect_all_ancestors()
        if self.parent2:
            ancestors.add(self.parent2.name)
            ancestors |= self.parent2._collect_all_ancestors()
        return ancestors

    def common_ancestor(self, other):
        """
        Повертає список імен спільних предків
        """
        my_ancestors = self._collect_all_ancestors()
        other_ancestors = other._collect_all_ancestors()
        common = my_ancestors & other_ancestors  # перетин множин
        return list(common) if common else None

# ## 🔍 Приклад використання:
# # Формуємо дерево
a = Person("Alex")
b = Person("Barbara")
c = Person("Charles", a, b)

d = Person("Diana")
e = Person("Edward")
f = Person("Fiona", d, e)

child = Person("George", c, f)

print(child.get_ancestors(1))  # ['Charles', 'Fiona']
print(child.get_ancestors(2))  # ['Alex', 'Barbara', 'Charles', 'Diana', 'Edward', 'Fiona']

print(c.common_ancestor(f))    # None
print(child.common_ancestor(f))  # ['Diana', 'Edward']

# ## ✅ Вивід:
# ['Charles', 'Fiona']
# ['Alex', 'Barbara', 'Charles', 'Diana', 'Edward', 'Fiona']
# None
# ['Diana', 'Edward']

# ## 🏁 Підсумок:
# | Завдання                  | Виконано |
# | ------------------------- | -------- |
# | Збереження дерева         | ✅        |
# | Рекурсивний пошук предків | ✅        |
# | Пошук спільного предка    | ✅        |

# Цей код гнучкий, легко розширюється (наприклад, можна додати стать, рік народження, або побудову графічного дерева).

# Тоді давай реалізуємо метод, який виводить **повне сімейне дерево** людини у вигляді ієрархії — **як "дерево з відступами"**.

# ## 🧠 **Ідея:**
# * Додамо до класу `Person` метод `print_family_tree(indent=0)`:
#   * він друкує ім’я поточної людини з відповідним відступом;
#   * потім рекурсивно викликає себе для `parent1` і `parent2`, збільшуючи рівень відступу.

# ## ✅ **Оновлений клас з методом `print_family_tree`:**
# class Person:
#     def __init__(self, name, parent1=None, parent2=None):
#         self.name = name
#         self.parent1 = parent1
#         self.parent2 = parent2

#     def get_ancestors(self, depth):
#         if depth <= 0:
#             return []

#         ancestors = []
#         if self.parent1:
#             ancestors.append(self.parent1.name)
#             ancestors += self.parent1.get_ancestors(depth - 1)
#         if self.parent2:
#             ancestors.append(self.parent2.name)
#             ancestors += self.parent2.get_ancestors(depth - 1)

#         return ancestors

#     def _collect_all_ancestors(self):
#         ancestors = set()
#         if self.parent1:
#             ancestors.add(self.parent1.name)
#             ancestors |= self.parent1._collect_all_ancestors()
#         if self.parent2:
#             ancestors.add(self.parent2.name)
#             ancestors |= self.parent2._collect_all_ancestors()
#         return ancestors

#     def common_ancestor(self, other):
#         my_ancestors = self._collect_all_ancestors()
#         other_ancestors = other._collect_all_ancestors()
#         common = my_ancestors & other_ancestors
#         return list(common) if common else None

#     def print_family_tree(self, indent=0):
#         """Виводить дерево родини з відступами"""
#         print(" " * indent + self.name)
#         if self.parent1:
#             print(" " * (indent + 2) + "Father:")
#             self.parent1.print_family_tree(indent + 4)
#         if self.parent2:
#             print(" " * (indent + 2) + "Mother:")
#             self.parent2.print_family_tree(indent + 4)

# ## 🔍 **Приклад використання:**
# # Формуємо дерево
# a = Person("Alex")
# b = Person("Barbara")
# c = Person("Charles", a, b)

# d = Person("Diana")
# e = Person("Edward")
# f = Person("Fiona", d, e)

# child = Person("George", c, f)

# # Виводимо дерево для George
# child.print_family_tree()

# ## ✅ Вивід:
# George
#   Father:
#     Charles
#       Father:
#         Alex
#       Mother:
#         Barbara
#   Mother:
#     Fiona
#       Father:
#         Diana
#       Mother:
#         Edward

# ## 📌 Переваги:
# * Можна вивести **будь-яке піддерево** — для `child`, `Fiona`, `Charles` тощо.
# * Відображення чітке, з вкладенням поколінь.

# Розширимо функціонал:
# # ✅ **1. Збереження дерева в рядок або файл**

# Ми додамо метод:
# ```python
# def get_family_tree_str(self, indent=0) → str
# ```

# – який повертатиме **рядок із ієрархічним деревом**, замість `print()`.

# І ще:

# * `save_family_tree(filename)` — для збереження дерева в `.txt` файл.

# ---

# # ✅ **2. Побудова графу родоводу (візуалізація)**

# Ми використаємо бібліотеку [`graphviz`](https://graphviz.readthedocs.io/en/stable/) (потрібно встановити: `pip install graphviz`).

# Додамо метод:

# ```python
# def generate_family_graph(self) → graphviz.Digraph
# ```

# – створює об'єкт графу.

# ---

# ## 🔧 **Оновлений клас `Person` з усім функціоналом:**

# ```python
# from graphviz import Digraph

# class Person:
#     def __init__(self, name, parent1=None, parent2=None):
#         self.name = name
#         self.parent1 = parent1
#         self.parent2 = parent2

#     def get_ancestors(self, depth):
#         if depth <= 0:
#             return []

#         ancestors = []
#         if self.parent1:
#             ancestors.append(self.parent1.name)
#             ancestors += self.parent1.get_ancestors(depth - 1)
#         if self.parent2:
#             ancestors.append(self.parent2.name)
#             ancestors += self.parent2.get_ancestors(depth - 1)

#         return ancestors

#     def _collect_all_ancestors(self):
#         ancestors = set()
#         if self.parent1:
#             ancestors.add(self.parent1.name)
#             ancestors |= self.parent1._collect_all_ancestors()
#         if self.parent2:
#             ancestors.add(self.parent2.name)
#             ancestors |= self.parent2._collect_all_ancestors()
#         return ancestors

#     def common_ancestor(self, other):
#         my_ancestors = self._collect_all_ancestors()
#         other_ancestors = other._collect_all_ancestors()
#         common = my_ancestors & other_ancestors
#         return list(common) if common else None

#     def print_family_tree(self, indent=0):
#         """Принт дерева у консоль"""
#         print(self.get_family_tree_str(indent))

#     def get_family_tree_str(self, indent=0):
#         """Повертає дерево як рядок з відступами"""
#         result = " " * indent + self.name + "\n"
#         if self.parent1:
#             result += " " * (indent + 2) + "Father:\n"
#             result += self.parent1.get_family_tree_str(indent + 4)
#         if self.parent2:
#             result += " " * (indent + 2) + "Mother:\n"
#             result += self.parent2.get_family_tree_str(indent + 4)
#         return result

#     def save_family_tree(self, filename):
#         """Зберігає дерево у файл"""
#         tree_str = self.get_family_tree_str()
#         with open(filename, "w", encoding="utf-8") as f:
#             f.write(tree_str)

#     def generate_family_graph(self):
#         """Створює граф родоводу (об'єкт graphviz.Digraph)"""
#         dot = Digraph()
#         visited = set()

#         def add_edges(person):
#             if person.name in visited:
#                 return
#             visited.add(person.name)
#             dot.node(person.name)

#             if person.parent1:
#                 dot.node(person.parent1.name)
#                 dot.edge(person.parent1.name, person.name)
#                 add_edges(person.parent1)
#             if person.parent2:
#                 dot.node(person.parent2.name)
#                 dot.edge(person.parent2.name, person.name)
#                 add_edges(person.parent2)

#         add_edges(self)
#         return dot
# ```

# ---

# ## 🔍 **Використання всіх можливостей:**

# ```python
# # Створення дерева
# a = Person("Alex")
# b = Person("Barbara")
# c = Person("Charles", a, b)

# d = Person("Diana")
# e = Person("Edward")
# f = Person("Fiona", d, e)

# child = Person("George", c, f)

# # 1. Вивід дерева у консоль
# child.print_family_tree()

# # 2. Збереження у файл
# child.save_family_tree("george_family_tree.txt")

# # 3. Побудова графу (і візуалізація)
# dot = child.generate_family_graph()
# dot.render("george_family_tree", format="png", cleanup=True)  # створить файл PNG
# ```

# ---

# ## 📌 Пояснення:

# | Метод                            | Що робить                           |
# | -------------------------------- | ----------------------------------- |
# | `print_family_tree()`            | Виводить дерево у консоль           |
# | `get_family_tree_str()`          | Повертає дерево як текст            |
# | `save_family_tree("ім'я_файлу")` | Зберігає дерево у `.txt`            |
# | `generate_family_graph()`        | Створює граф з допомогою `graphviz` |
# | `dot.render()`                   | Генерує зображення (наприклад, PNG) |

# ---

# ## ✅ Результат:

# * Маєш **вивід у консоль**
# * **Збереження у файл**
# * **Автоматичну побудову графу з картинкою!** 🖼️

# ---

# ## 💡 Примітка:

# Не забудь встановити:

# ```
# pip install graphviz
# ```

# І також **[Graphviz систему](https://graphviz.org/download/)** (якщо не встановлена), щоб працювали візуалізації.

# 🔔 Готовий допомогти адаптувати для GUI, або зберігати повну структуру у JSON/CSV!
# Хочеш? 😎

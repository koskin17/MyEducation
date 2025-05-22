# Cделаем адаптацию **XML → JSON**, как в реальной задаче, когда:
# * У нас есть данные в формате **XML**;
# * Нам нужно передать их в **машинное обучение или веб-приложение**, где нужен **JSON**;
# * При этом **ML-модель ничего не должна знать про XML**.

## ✅ Что сделаем
# 1. Класс `XMLData`: возвращает данные в XML.
# 2. Класс `JSONAdapter`: адаптирует XML → JSON.
# 3. Клиент (например, ML-система) получает только JSON.

## ✅ 📦 Упрощённый код с адаптером XML → JSON
import json
import xml.etree.ElementTree as ET

# Эмуляция внешнего XML-источника
class XMLData:
    def get_xml_string(self):
        return """
        <vehicle>
            <type>Car</type>
            <brand>Ford</brand>
            <model>Focus</model>
            <year>2020</year>
        </vehicle>
        """

# Адаптер для преобразования XML → JSON
class JSONAdapter:
    def __init__(self, xml_source):
        self.xml_source = xml_source

    def get_data(self):
        xml_string = self.xml_source.get_xml_string()
        root = ET.fromstring(xml_string)  # Разбираем XML
        result = {}

        for child in root:
            result[child.tag] = child.text  # Преобразуем XML-элементы в словарь

        return json.dumps(result, indent=4)  # Возвращаем JSON-строку


# Клиент, который "хочет только JSON"
def client_code(data_provider):
    print("ML-модуль получил данные:")
    print(data_provider.get_data())


# Тест
if __name__ == "__main__":
    xml_data = XMLData()
    adapter = JSONAdapter(xml_data)

    client_code(adapter)  # Используем адаптер вместо XML напрямую

## 🔍 Объяснение по шагам

### 1. `XMLData.get_data()`
# Это внешний источник (как API), который отдаёт **строку XML**:
# <vehicle>
#     <type>Car</type>
#     <brand>Ford</brand>
#     <model>Focus</model>
#     <year>2020</year>
# </vehicle>

### 2. `JSONAdapter`
# Это и есть **наш адаптер**.
# root = ET.fromstring(xml_string)
# * Преобразуем XML-строку в структуру XML-элементов (`ElementTree`).
# for child in root:
#     result[child.tag] = child.text

# * Пробегаем по каждому тегу (например, `<type>`, `<brand>`) и сохраняем их как ключ-значение в `dict`.
# return json.dumps(result, indent=4)
# * Преобразуем словарь в красивую **JSON-строку**.

### 3. `client_code(adapter)`
# Этот код не знает, что внутри был XML. Он вызывает `get_data()` и получает чистый JSON:
# {
#     "type": "Car",
#     "brand": "Ford",
#     "model": "Focus",
#     "year": "2020"
# }

## 🧠 Что мы доказали
# | Что было                   | Что стало                       |
# | -------------------------- | ------------------------------- |
# | Данные приходят в XML      | ML-система требует JSON         |
# | Проблема — несовместимость | Решение — `Adapter`             |
# | Прозрачность               | ML-клиент даже не знает про XML |

# Давай я расскажу тебе **подробно, но простыми словами**, что такое `xml.etree.ElementTree` в Python, **зачем он нужен**, и **как им пользоваться на практике**.

# ---

# ## 🧩 Что такое `xml.etree.ElementTree`?

# `xml.etree.ElementTree` — это **встроенный модуль Python**, который позволяет **работать с XML-файлами и строками**.

# ### XML — это:

# Формат хранения данных, похожий на HTML, например:

# ```xml
# <vehicle>
#     <type>Car</type>
#     <brand>Ford</brand>
#     <year>2020</year>
# </vehicle>
# ```

# ---

# ## ✅ Зачем нужен `ElementTree`?

# Он позволяет:

# * 📖 читать XML (из строки или файла);
# * 🔍 находить нужные теги (например, `<brand>`);
# * ✏️ изменять XML-структуру;
# * 📝 создавать XML «с нуля»;
# * 💾 сохранять в файл.

# ---

# ## 🔧 Основные функции и классы

# | Название                     | Что делает                                  |
# | ---------------------------- | ------------------------------------------- |
# | `ET.fromstring(xml_str)`     | Преобразует XML-строку в дерево (`Element`) |
# | `ET.parse(filename)`         | Загружает XML из файла                      |
# | `ET.Element(tag)`            | Создаёт элемент с тегом                     |
# | `ET.SubElement(parent, tag)` | Добавляет вложенный тег                     |
# | `ET.tostring(element)`       | Преобразует обратно в XML-строку            |
# | `element.find(tag)`          | Находит вложенный элемент                   |
# | `element.findall(tag)`       | Находит все элементы с таким тегом          |

# ---

# ## 🔍 Пример разбора XML

# ```python
# import xml.etree.ElementTree as ET

# xml_data = """
# <person>
#     <name>John</name>
#     <age>30</age>
# </person>
# """

# # Разбираем строку
# root = ET.fromstring(xml_data)

# print(root.tag)  # person
# print(root.find("name").text)  # John
# print(root.find("age").text)   # 30
# ```

# ---

# ## 🏗 Пример создания XML

# ```python
# import xml.etree.ElementTree as ET

# # Создаём корневой элемент
# person = ET.Element("person")

# # Вложенные элементы
# name = ET.SubElement(person, "name")
# name.text = "Alice"

# age = ET.SubElement(person, "age")
# age.text = "28"

# # Преобразуем в строку
# xml_str = ET.tostring(person, encoding='unicode')
# print(xml_str)
# ```

# 📤 Вывод:

# ```xml
# <person><name>Alice</name><age>28</age></person>
# ```

# ---

# ## 💾 Пример загрузки XML из файла

# ```python
# tree = ET.parse("data.xml")  # Открывает и парсит XML-файл
# root = tree.getroot()

# for child in root:
#     print(child.tag, child.text)
# ```

# ---

# ## 🧠 В чём сила `ElementTree`?

# * Встроен в Python — ничего устанавливать не нужно.
# * Очень простой — легко освоить новичку.
# * Умеет и читать, и писать, и изменять XML.

# ---

# Хочешь — могу показать, как с помощью `ElementTree`:

# * удалить теги,
# * добавить атрибуты,
# * сохранить XML в файл красиво с отступами.

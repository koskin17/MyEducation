# Подключиться к **PDF-файлу в Python** можно с помощью специальных библиотек, которые позволяют **извлекать, редактировать и анализировать содержимое PDF**.  

### ✅ **Лучшие библиотеки для работы с PDF в Python:**  
# 1️⃣ **PyMuPDF (`fitz`)** → Быстрая работа с текстом и изображениями:  
import fitz  # PyMuPDF

doc = fitz.open(r"E:\My project\MyEducation\Softserve\UA-130 Advanced Python with Django\Sprint 10 Database\Quiz Data Base Python SQLAlchemy.pdf")
text = ""
for page in doc:
    text += page.get_text("text")  # Извлекаем текст
print(text)

# 2️⃣ **pdfplumber** → Отлично подходит для извлечения сложных таблиц и форматированного текста:  
# import pdfplumber

# with pdfplumber.open(r"E:\My project\MyEducation\Softserve\UA-130 Advanced Python with Django\Sprint 10 Database\Quiz Data Base Python SQLAlchemy.pdf") as pdf:
#     first_page = pdf.pages[0]
#     print(first_page.extract_text())  # Получаем текст первой страницы

# 3️⃣ **PyPDF2** → Подходит для объединения, разбиения и шифрования PDF:  
# import PyPDF2

# with open(r"E:\My project\MyEducation\Softserve\UA-130 Advanced Python with Django\Sprint 10 Database\Quiz Data Base Python SQLAlchemy.pdf", "rb") as file:
#     reader = PyPDF2.PdfReader(file)
#     text = "\n".join([page.extract_text() for page in reader.pages])
#     print(text)

# 4️⃣ **pdfrw** → Если нужно **редактировать PDF** (например, добавлять аннотации).  
# 5️⃣ **pdf2image** → Конвертация страниц PDF **в изображения (PNG, JPG, etc.)**.  

# 📌 **Какой метод лучше выбрать?**  
# 🔹 **Если нужен текст** → Используй **PyMuPDF или pdfplumber**.  
# 🔹 **Если нужно редактировать PDF** → Используй **PyPDF2 или pdfrw**.  
# 🔹 **Если PDF содержит таблицы** → Используй **pdfplumber**.  

# Если код выполняется без ошибок, но выводится **пустая строка**, то, скорее всего:  

# 🔹 **PDF-файл пустой** или **не содержит извлекаемого текста**.  
# 🔹 **Текст внутри PDF представлен как изображение** (например, отсканированный документ).  
# 🔹 **Выбран неправильный метод для извлечения текста**.  

# ### ✅ **Решение проблемы**  

# 1️⃣ **Проверка, есть ли текст в PDF**  
# Попробуй **открыть PDF вручную** и попробуй **скопировать текст**.  
# Если текст **не копируется**, это означает, что он **является изображением**, и для его обработки нужен `OCR` (распознавание текста).  

# 📌 **Проверка количества страниц в PDF**  
# Попробуй этот код, чтобы убедиться, что PDF-файл не пустой:  
# ```python
# import PyPDF2

# with open("E:/My project/MyEducation/Softserve/UA-130 Advanced Python with Django/Sprint 10 Database/Quiz Data Base Python SQLAlchemy.pdf", "rb") as file:
#     reader = PyPDF2.PdfReader(file)
#     print(f"Количество страниц: {len(reader.pages)}")
# ```
# 🔹 **Если `len(reader.pages) == 0`**, PDF-файл повреждён или пуст.  

# 2️⃣ **Попробуй `pdfplumber` вместо `PyPDF2`**  
# ```python
# import pdfplumber

# with pdfplumber.open("E:/My project/MyEducation/Softserve/UA-130 Advanced Python with Django/Sprint 10 Database/Quiz Data Base Python SQLAlchemy.pdf") as pdf:
#     for page in pdf.pages:
#         print(page.extract_text())  # Извлечение текста
# ```
# 🔹 **`pdfplumber` лучше работает с таблицами и сложными PDF-документами**.  

# 3️⃣ **Если текст не извлекается, нужен OCR (распознавание текста)**  
# Если PDF содержит **изображения с текстом**, попробуй использовать **Tesseract OCR**:  
# import pytesseract
# from pdf2image import convert_from_path

# # Конвертация PDF в изображение
# images = convert_from_path(r"E:/My project/MyEducation/Softserve/UA-130 Advanced Python with Django/Sprint 10 Database/Quiz Data Base Python SQLAlchemy.pdf")

# # Распознавание текста на первой странице
# text = pytesseract.image_to_string(images[0], lang="ukr")
# print(text)

# 📌 **Убедись, что Tesseract OCR установлен** ([скачать](https://github.com/tesseract-ocr/tesseract)).  

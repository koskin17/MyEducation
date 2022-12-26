import wikipedia


# Получение страницы
python_page = wikipedia.page('victory')

# # html-код страницы
# print(python_page.html)
#
# # Заголовок статьи
# print(python_page.original_title)

# Краткое содержание
print(python_page.summary)

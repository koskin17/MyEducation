# John wants to filter all the verses in a specific chapter in the Bible by the verse id. The Bible has 66 books, each book has a lot of chapters, and each chapter has a lot of verses.

# The pattern of the id is bbcccvvv, where:

# bb is the Book ID. (01 < bb ≤ 66);
# ccc is the Chapter ID. (001 ≤ ccc);
# vvv is the Verse ID. (001 ≤ vvv).
# John wants to find verses that belong to the Book and Chapter, given by their IDs.

# Example:
# If John's scriptures are ["01001001", "01001002", "01002001", "01002002", "01002003", "02001001", "02001002", "02001003"], then
# filterBible(scripture, "01", "001") => ["01001001","01001002"]

# [input] array.string scripture

# An array of the scriptures' ids, sorted by ASC.

# [input] string book

# Book id (2 letters)

# [input] string chapter

# Chapter id (3 letters)

# [output] array.string

# A filtered array with verses from the given chapter in the given book of the Bible.

def filterBible(scripture, book, chapter):
    prefix = book + chapter  # Формируем префикс (например, "01" + "001" = "01001")
    # Отбираем те строки, которые начинаются с этого префикса
    filtered_verses = [verse for verse in scripture if verse.startswith(prefix)]
    return filtered_verses

# Пример использования:
scripture = [
    "01001001", "01001002", "01002001", 
    "01002002", "01002003", "02001001", 
    "02001002", "02001003"
]
result = filterBible(scripture, "01", "001")
print(result)  # Ожидаемый вывод: ["01001001", "01001002"]
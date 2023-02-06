string_01 = "History is always written by the wunners." \
            "When two culture clash, the loser is obliterated, and"

# Получение длины строки за вычетом пробелов, запятых и точек
print(len(string_01) - string_01.count(' ') - string_01.count(',') - string_01.count('.'))
# Подсчет кол-ва слов в строке
print(string_01.split(" "))
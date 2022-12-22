##file = open("text.txt", "r+", encoding='utf-8')
##print(file.readlines())

with open("text_for_analyzer.txt") as f:
    text = f.read()
'''
Функция подсчёта количества символов в тексте
'''


def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count


print(text)
print('')

x = input('Введите искомый символ для поиска в тексте:')
print('Символ "{0}" в тексте встречается {1} раз(а)'.format(x, count_char(text, x)))
'''
Цикл для подсчёта процента, который каждый символ занимает в тексте
'''
print('Процентное соотношение по всем символам в тексте:')
for char in "abcdefghijklmnopqrstuvwxyz":
    perc = 100 * count_char(text, char) / len(text)
    print("{0} - {1}%".format(char, round(perc, 2)))

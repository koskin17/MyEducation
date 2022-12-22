u = (' Это строка, которую я хочу разделить на слова, отбрасывая все пробелы')
y = u.strip()
print(y)
print('')

y = y.split(' ')
print(y)
print('')

words = {}
for word in y:
    try:
        words[word] += 1
    except KeyError:
        words[word] = 1
print(words)
pairs = words.items()
print(pairs)

txt = input('Введите текст: ')
txt = txt.split(' ')

'''
Функция подчета количества слов в тексте
'''
def count_word(text):
  count = 0
  for word in text:
      count += 1
  return count

print('Кол-во слов в тексте: ', count_word(txt))
'''
После применения функции split к переменной с текстом
можно использовать функцию подсчёта длинны len
'''
print(len(txt))

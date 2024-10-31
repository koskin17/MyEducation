# http://python-lab.blogspot.com/2012/05/difflib.html

import difflib

lst = ['vasiliy', 'sasha', 'vasyan', 'barbara', 'r']
# Определение похожих слов
print("Похожи слова со словом 'vasya':", difflib.get_close_matches('vasya', lst, n=2))

print()
text1 = """Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Integer
  2: eu lacus accumsan arcu fermentum euismod. Donec pulvinar porttitor
  3: tellus. Aliquam venenatis. Donec facilisis pharetra tortor.  In nec
  4: mauris eget magna consequat convallis. Nam sed sem vitae odio
  5: pellentesque interdum. Sed consequat viverra nisl. Suspendisse arcu
  6: metus, blandit quis, rhoncus ac, pharetra eget, velit. Mauris
  7: urna. Morbi nonummy molestie orci. Praesent nisi elit, fringilla ac,
  8: suscipit non, tristique vel, mauris. Curabitur vel lorem id nisl porta
  9: adipiscing. Suspendisse eu lectus. In nunc. Duis vulputate tristique
 10: enim. Donec quis lectus a justo imperdiet tempus."""

text2 = """Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Integer
 14: eu lacus accumsan arcu fermentum euismod. Donec pulvinar, porttitor
 15: tellus. Aliquam venenatis. Donec facilisis pharetra tortor. In nec
 16: mauris eget magna consequat convallis. Nam cras vitae mi vitae odio
 17: pellentesque interdum. Sed consequat viverra nisl. Suspendisse arcu
 18: metus, blandit quis, rhoncus ac, pharetra eget, velit. Mauris
 19: urna. Morbi nonummy molestie orci. Praesent nisi elit, fringilla ac,
 20: suscipit non, tristique vel, mauris. Curabitur vel lorem id nisl porta
 21: adipiscing. Duis vulputate tristique enim. Donec quis lectus a justo
 22: imperdiet tempus. Suspendisse eu lectus. In nunc. """

# Класс Differ работает с последовательностями строк и выводит разницу между ними.
# Для этого разбивает текст на строки.
text1_lines = text1.splitlines()
text2_lines = text2.splitlines()

# Создаём объект difflib.Differ()
d = difflib.Differ()
# Вызываем метод compare для сравнения двух текстов
diff = d.compare(text1_lines, text2_lines)

"""
В результатах сравнения:
- Знак "-" означает, что эта строка присутствует в первой последовательности, но отсутствует во второй.
- Знак "+" означает, что строка присутствует во второй последовательности, но не в первой.
Если в строке есть дополнительные изменения в новой версии,
то в выводе будет присутствовать строка со знаком "?", в которой будут помечены эти изменения.
Если строка не изменилась, она выводится с дополнительным отступом слева так,
что она будет располагаться на том же уровне, что и строки с изменениями."""

print('\n'.join(diff))

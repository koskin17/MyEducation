file = open("books.txt", "w+", encoding='utf-8')

file.write('Harry Potter\n')
file.write('Some book\n')
file.write('Another book\n')
file.write('Третья книга\n')
file.write('Четвёртая книга\n')
file.write('Пятая книга')

file = open("books.txt", "r", encoding='utf-8')

for string in file:
    string = string.strip()
    s1 = str(string[0])
    s2 = str(len(string))
    print(s1 + s2)

file.close()

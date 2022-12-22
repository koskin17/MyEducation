file = open('test.txt', 'w')

for i in range(10):
    string = 'Строка № ' + str(i) + '\n'
    file.write(string)

file.close()

file = open('test.txt', 'r')
line = file.readline()

while line != '':
    print(line.rstrip('\n'))
    line = file.readline()

file.close()

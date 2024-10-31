file = open('table.doc', 'r+', encoding='utf-8')
file_string = []
for line in file:
    fstring = line.strip('\n')
    file_string.append(fstring)

print(file_string) 

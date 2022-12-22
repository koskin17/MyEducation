customers, n = [2,2,3,3,4,4], 2                 # дана очередь из людей, в которой цифры означают время работы каждого с кассой, и дано кол-во касс

def queue_time(customers, n):
    if len(customers) == 0:                         # Если в очереди никого нет, то и время обслуживания равно нулю
        return 0
    if len(customers) == n or len(customers) < n:   # Если очередь меньше, чем кол-во касс, или равно кол-ву касс, то общее время обслуживания будет равно максимальному времени работы с
                                                    # кассой одного из тех, кто в очереди
        return max(customers)

    area = []                                       # Делаем мнимый зал касс
    time = 0                                        # Счетчик для суммирования времени работы с кассами
    index = n                                       # Фиксируем индекс первого человека, который первый зайдёт на замену первому закончившему пользоваться кассой

    for i in range(n):                              # Делаем мнимый список людей, равный числу касс, которые как бы зашли в зал касс и начали с ними работать 
        area.append(customers[i])

    for i in range(n, len(customers)):
        mintime = min(area)
        time += mintime

        for y in range(len(area)):
            if area[y] - mintime == 0:
                area[y] = customers[index]
                index += 1
            else:
                area[y] -= mintime

            if index == len(customers):
                time += max(area)
                return time

            
print(queue_time(customers, n))

''' Второй вариант '''

def queue_time(customers, n):
    checkout_list=[]
    for i in range(n):
        checkout_list.append(0)
    for i in customers:
        checkout_list.sort()
        checkout_list[0] += i
        print(checkout_list)
    return max(checkout_list)

queue_time(customers, n)

''' Третий вариант '''

def queue_time(customers, n):
    l=[0]*n
    for i in customers:
        l[l.index(min(l))]+=i
    return max(l)



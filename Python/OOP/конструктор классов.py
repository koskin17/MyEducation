'''
Конструкторы класса.
Классы принято создавать в отдельном файле.
После этот файл импортировать в основной код программы:

import classes

Если используется метод импортирования всех классов,
то для получения доступа к конкретному классу
в коде нужно чётко указывать:

person1 = classes.Person()

Можно импортировать классы.
from classes import Person, next и т.д.

Тогда в коде просто указывается имя класса:

person1 = Person()



'''
##import classes
##
##person1 = classes.Person('John') # создаём экземпляр класса
##person1.print_info()
##
##person1 = classes.Person('Katy') # создаём экземпляр класса
##person1.print_info()


from OOP.Egorov.classes import Person

person1 = Person('John')    # создаём экземпляр класса
person1.print_info()

person2 = Person('Katy')    # создаём экземпляр класса
person2._Person__age = 30   # при такой записи подчеркивание+имя Класса+2 подчёркивания+имя свойства
                            # значение свойства всё-таки можно изменить
person2.print_info()
''' Получаем значение свойства методом get '''
print(person2.get_age())

''' Устанавливает значение свойства методом set '''
person2.set_age(55)
''' Выводим изменённое значение свойства '''
person2.print_info()

''' Получение значение свойства при помощи декоратора,
    который делает из метода метод геттер. '''
print(person2.age)

''' Изменение свойства age при помощи декораторов '''
print()
print('Был возраст:')
person2.print_info()
print('Устанавливаем возраст 85')
person2.age = 85
print('Стал возраст:')
person2.print_info()




import random

''' Создаём список для случайного первоначального положения
монеты '''
side = ['Орёл','Решка']

class Coin:  
    ''' Определяем случайное первоначальное положение монеты '''
    def __init__(self):
        self.__sideup = random.choice(side)

    def toss(self):
        if random.randint(0,1) == 0:
            self.__sideup = 'Орёл'
        else:
            self.__sideup = 'Решка'

    def get_sideup(self):
        return self.__sideup

from module import print_water_state

global FREEZING_POINT
global BOILING_POINT

FREEZING_POINT = 0
print(FREEZING_POINT)
BOILING_POINT = 100
print(BOILING_POINT)


user_temp = int(input("Введите градусы: "))
print_water_state(user_temp)


# Получение нескольких наибольших и наименьших значений в последовательности

import heapq

print("Модуль heapq автоматически определяет наибольшие / наименьшие значения в последовательности и возвращает их"
      " в виде списка.")
print("5 наибольших значений в range(100):", heapq.nlargest(5, range(100)))
print("Одно наибольшее значение в range(20):", heapq.nlargest(1, range(20)))
print("3 наибольших значения в range(100) с шагом 10:", heapq.nlargest(3, range(0, 100, 10)))
print()
print("5 наименьших значений в range(100):", heapq.nsmallest(5, range(100)))
print("Одно наименьшее значение в range(1, 20):", heapq.nsmallest(1, range(1, 20)))
print("3 наименьших значения в range(100) с шагом 10:", heapq.nsmallest(3, range(0, 100, 10)))

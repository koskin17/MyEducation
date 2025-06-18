import math
def frectangle (l,w):
    return l*w
def fcircle (r):
    return  math.pi * r ** 2
def ftriangle(he,basis):
    return 0.5* basis* he
choice  = input("Вибиріть фігуру (rectangle, triangle, circle): ")
if choice  == "rectangle":
    l = float(input("Ведіть довжину "))
    w = float(input("Ведіть ширину "))
    print(l) 
    print(w)
    print(frectangle(l,w))
elif choice  == "triangle":
    he = float(input("Ведіть висоту "))
    basis = float(input("Ведіть основу "))
    print(ftriangle(he,basis))
elif choice  == "circle":
    r  = float(input("Ведіть Радіус "))
    print(fcircle(r))
else:
    print("неправильно вибрано ")
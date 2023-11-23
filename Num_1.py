from math import *

# №1

# x=3
# y=4
# z=5
# a=(sqrt(abs((pow(x,2))-6))-sqrt(abs((pow(y,2))-5)))/(1+((pow(x,2))/((pow(y,3))+1))+((pow(y,2))/((pow(x,3))+1)))
# b=(pow(x,3))*((pow(atan(z),3))+exp(1))
# print(f"Функция а: {a}")
# print(f"Функция b: {b}")

# №2
# a=2
# b=-1
# c=3
#
# x=-0.5
# while x <=-0.4:
#     F=pow(x+a,1/3)+((c*(pow(x,2)))/(b+x))
#     print(f"Функция f(x)= {F}")
#     x+=0.1

# №3

x=1
while x <= 3:
    F=pow(cos(sin(1/pow(x,2))),2)
    print(F)
    x+=0.1

# №4

# x1=2
# x2=4
# x3=6
#
# y1="L"
# y2=2
# y3=6
#
# a=sqrt(pow(x2-x1,2)+pow(y2-y1,2))
#
# print(f"Периметр ромба равен: {a*4}")
# b=sqrt(pow(x3-x1,2)+pow(y3-y1,2))
# c=sqrt(pow(x3-x2,2)+pow(y3-y2,2))
#
# P=(a+b+c)/2
# S=2*sqrt(P*(P-a)*(P-b)*(P-c))
# print(f"Площадь ромба равна: {S}")

# №5

# v1=5
# v2=4
# t1=36
# t2=42
#
# V=v1+v2
# T=(t1*v1+t2*v2)/V
#
# print(f"Объём: {V}, Температура: {T}")

# №6


# a=int(input("Введите а: "))
# while a<1:
#     a = int(input("Число не должно быть меньше 1, повторите ввод: "))
# b=int(input("Введите b: "))
# c=int(input("Введите c: "))
# while c>100:
#     c = int(input("Число не должно быть больше 100, повторите ввод: "))
#
# V=a*b*c
# S=2*(a*b+a*c+c*b)
# print(f"Объем, площадь: {V:.4f} {S:.4f}")

# №7

# x1 = int(input("Введите x1: "))
# while x1<-10:
#      x1 = int(input("Число не должно быть меньше -10, повторите ввод: "))
# x2 = int(input("Введите x2: "))
# x3 = int(input("Введите x3: "))
#
# y1 = int(input("Введите y1: "))
# y2 = int(input("Введите y2: "))
# y3 = int(input("Введите y3: "))
# while y3>10:
#      y3 = int(input("Число не должно быть больше 10, повторите ввод: "))
#
# a = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
# b = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
# c = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
# P = (a + b + c) / 2  # Находим полупериметр
# S = (P * (P - a) * (P - b) * (P - c)) ** 0.5
# P *= 2
# print(f"Периметр, площадь: {P:.3f} {S:.3f}")

# №8

# v1 = int(input("Введите скорость первого автомобиля: "))
# while v1<1:
#      v1 = int(input("Скорость не должна быть меньше 1, повторите ввод: "))
# v2 = int(input("Введите скорость второго автомобиля: "))
# S = int(input("Введите расстояние между автомобилями: "))
# T = int(input("Введите прошедшее время: "))
# while T>100:
#      T = int(input("Скорость не должна быть больше 100, повторите ввод: "))
#
# S_otvet=S+v1*T+v2*T
# print(f"Расстояние между автомобилями через {T:.4f} часов равно:{S_otvet:.4f} км")

# №9

# cerosin_count=5
# days=24
# hours=6
# cerosin=120
#
# chas_pyat=cerosin/144
# cerosin_by_hour=chas_pyat/cerosin_count
# nine_cerosin_by_hour=cerosin_by_hour*9
# day_cerosin=nine_cerosin_by_hour*8
# print(f"Всего пять керосинок горело: {days*hours:.2f}(ч)")
# print(f"В час на пять керосинок уходило: {chas_pyat:.2f}(л)")
# print(f"На одну керосинку в час уходило: {cerosin_by_hour:.2f}(л)")
# print(f"На девять керосинок в час будет уходить: {nine_cerosin_by_hour:.2f}(л)")
# print(f"В день (8ч) на девять керосинок надо: {day_cerosin:.2f}(л)")
# print(f"Тогда, 216л керосина хватит на: {216/day_cerosin:.2f}(дней)")
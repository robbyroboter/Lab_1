from math import *
# №1

x=3
y=4
z=5
a=(sqrt(abs((x^2)-6))-sqrt(abs((y^2)-6)))/(1+((x^2)/((y^3)+1))+((y^2)/((x^3)+1)))
b=(x^3)*((pow(atan(z),3))+exp(1))
print(a)
print(b)

# №2
# a=2
# b=-1
# c=3
#
# x=-0.5
# while x <-0.4:
#     F=pow(x+a,1/3)+((c*(pow(x,2)))/(b+x))
#     print(F)
#     x+=0.1

# №3

# x=1
# while x <3:
#     F=pow(cos(sin(1/pow(x,2))),2)
#     print(F)
#     x+=0.1

#№4 *

# x1=2
# x2=4
# x3=6
#
# y1=2
# y2=4
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

#№5

# v1=5
# v2=4
# t1=36
# t2=42
#
# V=v1+v2
# T=(t1*v1+t2*v2)/V
#
# print(f"Объём: {V}, Температура: {T}")

#№6

# a=1
# b=4
# c=100
#
# V=a*b*c
# S=2*(a*b+a*c+c*b)
# print(f"Объем, площадь: {V:.4f} {S:.4f}")

#№7

# x1=-10
# x2=4
# x3=6
#
# y1=2
# y2=4
# y3=10
#
# a = ((x1-x2)**2 + (y1-y2)**2)**0.5
# b = ((x1-x3)**2 + (y1-y3)**2)**0.5
# c = ((x3-x2)**2 + (y3-y2)**2)**0.5
# P = (a + b + c)/2
# S = (P*(P - a)*(P - b)*(P - c))**0.5
# P*=2
# print(f"Периметр, площадь: {P:.3f} {S:.3f}")
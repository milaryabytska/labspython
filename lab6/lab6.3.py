"n - вимірність простору"
"suma1 - сума елементів 1-го вектора піднесених до квадрату"
"suma2 - сума елементів 2-го вектора піднесених до квадрату"
"skalyar - скалярний добуток 2 векторів"
"x - елементи 1-го вектора"
"y - елементи 2-го вектора"
"modul1 - довжина 1-го вектора"
"modul2 - довжина 2-го вектора"
"cosinus - косинус кута між векторами"
""""""

from math import *
n = int(input("Введіть вимірність простору : "))
suma1 = 0
suma2 = 0
skalyar = 0
x = [float(input("Введіть {0} елемент 1-го вектора : ".format(i))) for i in range(1, n+1)]
y = [float(input("Введіть {0} елемент 2-го вектора : ".format(i))) for i in range(1, n+1)]
for i in range(n):
    suma1 += x[i]**2
    suma2 += y[i]**2
    skalyar += x[i]*y[i]
modul1 = sqrt(suma1)
modul2 = sqrt(suma2)
cosinus = skalyar/(modul1*modul2)
print("Косинус кута між двома векторами = {0}".format(cosinus))
if cosinus == 0:
    print("Вектори є перпендикулярними")
else:
    print("Вектори не є перпендикулярними")

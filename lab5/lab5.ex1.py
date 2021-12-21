# позначення
'''
сума             suma
натуральне число  n
дійсне число      x
'''
# введення даних
import math
n=int(input('Введіть n: '))
x=float(input('Введіть x:'))
suma=0
while n>0:
    suma+=math.cos(x)**n
    n-=1
# виведення даних
print('Cума= {0:.2f}'.format(suma))



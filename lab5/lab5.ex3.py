from math import*
x=int(input('введіть значення x: '))
n=int(input('введіть значення n: '))
suma=0
m=1
for i in range(1,n+1):
    suma+=sin((m*x)/m)
    m+=1
suma*=2
print('Розв\'язок{0}'.format (suma))

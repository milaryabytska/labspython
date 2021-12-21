# позначення
'''
перше дійсне число a
друге дійсне число b
третє дійсне число c
максимум          max
мінімум           min
сума              suma
'''
# введення даних
a=float(input('a= '))
b=float(input('b= '))
c=float (input('c= '))
if a>b:
    max=a
else:
    max=b
if b<c:
    min=b
else:
    min=c
suma=max(a,b)+min((b,c))**2
# виведення даних
print ('Сума'{0}.format(suma))



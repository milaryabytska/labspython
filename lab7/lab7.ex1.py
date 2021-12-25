#Визначити добуток додатних парних елементів матриці.
import random
num_rows=int(input('введіть кількість рядків: '))
num_columns=int(input('введіть кількість стовпців: '))
a=[[random.randint(-10,10) for j in range(num_rows)]for i in range(num_columns)]
print(a)
i=0
j=0
result=1
for i in a:
    for j in i:
        if j>0 and j%2==0:
            result*=j
print(result)



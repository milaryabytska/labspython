# позначення
'''
перше натуральне число    x
друге натуральне число    y
'''
# введення даних
x=int(input('введіть перше число: '))
y=int(input('Введіть друге число: '))
counter1=0
counter2=0
while x%10==0:
    counter1+=1
    x=x//10
    break
while y%10==0:
    counter2+=1
    y=y//10
    break
if counter1>counter2:
    print('Перше число містить більше нулів')
elif counter1<counter2:
    print('Друге число містить більше нулів')
else:
    print('Однаково')




x0=x1=7
xi=0
i=int(input('введіть значення i: '))
if i<2:
    print('1')
else:
    for i in range (2,i+1):
        xi=x1*(1+x0)
        x0=x1
        x1=xi
print(xi)

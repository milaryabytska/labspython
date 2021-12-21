n=int(input('введіть і: '))
def factorial(i):
    if i==0:
        return 0
    elif i==1 or i==2:
        return 9
    return factorial(i-1)+(i-2)+(i-3)
print(factorial(n))

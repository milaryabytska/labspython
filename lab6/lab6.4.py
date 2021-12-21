a=[]
n=int(input('elementy: '))
for el in range(n):
    if el%2==1:
        a.append(el)
for elem in range(n):
    if elem%2==0:
        a.append(elem)
print(a)


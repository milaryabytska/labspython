#Дано матрицю  і число . Знайти добуток числа на матрицю.
a=3
A= [ [1,3,2], [3,7,5], [9,7,4]]
for row in A:
    for elem in row:
        B=map(lambda elem:elem*a, A)
print(B)

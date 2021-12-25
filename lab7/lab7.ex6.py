matr=[
    [1,2,3,4,9,5,10,11],
    [2,7,8,3,7,3,1,9],
    [3,4,2,-6,-9,37,28,7],
    [1,2,1,3,4,6,4,7],
    [8,9,4,5,3,19,67,56],
    [7,9,67,34,87,12,2,3],
    [9,8,5,4,7,3,7,9],
    [7,90,23,76,45,12,2,3]
]
suma=0
for i in range(len(matr)):
    for j in range(len(matr[i])):
        if matr[i][j]<0:
            el = matr.index(matr[i][j])
            suma+= matr[i][el]
print(suma)
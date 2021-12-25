A=[
    [9,2,3],
    [2,7,3],
    [5,1,8]
]
rows=3
columns=3
for i in range(rows):
    for j in range(columns):
        if int(j)%2==0:
            (A[j]).sort(reverse=True)

print(f'{A}')
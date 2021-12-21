a=[1,2,3,6,7,9,10,11]
for i in range(len(a)):
    for j in range (i+1, len(a)):
        d=a[j]-a[i]
        if a[j]+d in a:
            print(a[i],a[j],a[j]+d)


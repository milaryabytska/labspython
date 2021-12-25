with open('TextFile1.txt') as f:
    r = f.readlines()
    print(r)
    for el in r:
        el=int(el)
        if el>0:
            print(el)
            m=int(m)
            m=min(el)
            print(m)



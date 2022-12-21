def ins_s(a):
    for x in range(1,len(a)):
        key = a[x]
        y=x-1

        while y >=0 and key<a[y]:
            a[y+1]=a[y]
            y-=1
        a[y+1]=key

a=[77,6,28,11]
ins_s(a)
print(a)            
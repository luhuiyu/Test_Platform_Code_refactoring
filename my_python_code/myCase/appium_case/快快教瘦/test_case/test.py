L=[1,2,3,4,5]
LL=['A','B','C']
L2 = len(LL)
i=0
for x  in range(len(L)):

    print(L[x],LL[i])
    i = i + 1
    if i >= L2:
        i = 0

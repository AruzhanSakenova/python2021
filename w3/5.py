a = list(map(int,input(). strip(). split()))
k = int(input())
k = k%len(a)
if k<0:
    k = abs(k)
    print(*a[k:],end =' ')
    #print(*a[0:k])
    exit()
else:
    k = abs(k)
    print(*a[-k:],end =' ')
    print(*a[0:-k])
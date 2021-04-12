a = list(map(int,input(). strip(). split()))
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if (a[i]<0 and a[j]<0) or (a[i]>0 and a[j]>0):
            print(a[i], a[j])
            exit()
        else : break
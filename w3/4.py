a = list(map(int,input(). strip(). split()))
b=0
for i in range(len(a)):
    if a[i]==0:
        b+=1
    else:
        print(a[i])
for i in range(b):
    print(0, end=" ")
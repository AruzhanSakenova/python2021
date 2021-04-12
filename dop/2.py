a = list(map(int,input(). strip(). split()))
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[j]>a[i]:
           print(a[j])
           break
    
        
            
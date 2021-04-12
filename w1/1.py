n=int(input())
m=int(input())
if m>n:
    if m%n!=0:
        print(int(m/n)+1)
    else:
        print(int(m/n))
else:
    print(1)
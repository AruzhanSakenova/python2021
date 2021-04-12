n=int(input())
sl={}
for i in range(n):
    a,b=input().split()
    sl[a]=b
    sl[b]=a
p=str(input())
print(sl[p])
a=int(input())
b=int(a/60)
if b>=24:
    c=int(b/24)
    e=b-24*c
    print(e)

else:
    print(b)

print(a%60)
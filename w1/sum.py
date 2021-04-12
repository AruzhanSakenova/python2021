a=int(input())
b=a%10
c=a%100
d=a%1000
e=int((c-b)/10)
f=int((d-c)/100)
sum=b+e+f
print(sum)
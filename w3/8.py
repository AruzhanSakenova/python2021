n=int(input())
m=int(input())
a=set(input().split())
b=set(input().split())
print(len(a.intersection(b)))
print(a.intersection(b))
print(n-len(a.intersection(b)))
print(m-len(a.intersection(b)))
print(a.symmetric_difference_update(b))
print(b.symmetric_difference_update(a))


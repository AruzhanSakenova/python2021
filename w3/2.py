a = list(map(int,input(). strip(). split()))
min=11100000
for i in a:
    if min > i and i > 0:
        min= i
print(min)
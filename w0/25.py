#anagram hello olehl
line1, line2= input().split()
print(set(line1))
print(set(line2))
if set(line1)==set(line2):
    print('yes')
else:
    print('no')


if sorted(line1)==sorted(line2):
    print('yes')
else:
    print('no')
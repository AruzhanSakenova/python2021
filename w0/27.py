a=[2,3,4]
b=a.copy() #если пишем копи то выведется разнное
b.append(5)
b.append(7)
print(a)
print(b)
print(a is b) #являются ли одной ссылкой
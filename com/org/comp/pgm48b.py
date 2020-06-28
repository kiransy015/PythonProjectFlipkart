# wap to remove duplicate elements from a list

a = [10,30,40,60,70,30]
b = []

for i in a :
    if i not in b:
        b.append(i)
print(a)
print(b)

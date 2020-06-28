# wap to remove all duplicat characters from a string

str = "Python and selenium automation"
s=""

for ele in str:
    if ele not in s:
        s=s+ele
print(s)
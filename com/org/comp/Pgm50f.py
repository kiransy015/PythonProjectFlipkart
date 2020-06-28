str = "Python and selenium automation"
d = {}

for i in range(0,len(str),1):
    if str[i] in d:
        cnt = d.get(str[i])
        cnt=cnt+1
        d.update({str[i]:cnt})
    else:
        d.update({str[i]:1})
print(d)

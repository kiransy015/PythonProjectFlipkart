str = "Python and selenium automation"
s = str.split(" ")
r_str=""

for i in range(len(s)-1,-1,-1):
    r_str=r_str+s[i]+" "
print(r_str)
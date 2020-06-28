str = "Python and selenium automation"
s = str.split(" ")
strrev=""

for i in range(0,len(s),1):
    rev = s[i]
    for j in range(len(rev)-1,-1,-1):
        strrev=strrev+rev[j]
    strrev=strrev+" "

print(strrev)
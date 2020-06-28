# wap to replac a particular pattern in a string

str="Python and selenium automation"
s = str.replace(" ","$")
print(s)

rep=""
for i in range(0,len(str),1):
    if str[i]==' ':
        rep=rep+'$'
    else:
        rep=rep+str[i]

print(rep)


# How to get index of a particular character
str = "Python and Selenium Automation"
print(str.index('o'))

# How to count a particular character in a string
str = "Python and Selenium Automation"
print(str.count('o'))
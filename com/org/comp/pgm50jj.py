# wap to replace the pattern in a string without using inbuilt functionality

str = 'Python and selenium automation and training'
lst = str.split(' ')
str_temp=''

for i in lst:
    if i=='and':
        str_temp=str_temp+' '+'or'
    else:
        str_temp=str_temp+' '+i

print(str)
print(str_temp)

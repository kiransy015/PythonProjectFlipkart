str = 'Developer'
r_str=''
size = len(str)

for i in range(size-1,-1,-1):
    r_str=r_str+str[i]
print(r_str)

# converting character to upper and lower case
str = 'Developer'
s=str.upper()
print("After converting to upper case:",s)

str='DEVELOPER'
s = str.lower()
print("After converting to lower case:",s)

# how to chk the string case
str = "DEVELOPER"
print(str.isupper())
str="DEVELOPER"
print(str.islower())
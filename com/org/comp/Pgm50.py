# Printing very characters of a string
s = 'India'
size = len(s)

# approach1
for i in range(0,size):
    print(s[i])

# approach2
for element in s:
    print(element)

# Printing a string in reverse order
for i in range(size-1,-1,-1):
    print(s[i])
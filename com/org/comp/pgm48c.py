# wap to search an element in a list

lst = [10,20,30,40,50,40]
a = int(input('Enter the element to search:'))
size = len(lst )
status=False

for i in range(0,size):
    if lst[i]==a:
        status=True
        break

if(status):
    print("Element is present")
else:
    print("Element is not present")
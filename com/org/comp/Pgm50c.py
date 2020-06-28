# wap to count available VOVELS in a string
str='Python and selenium Automation'
count = 0

for s in str:
    if s in ['a','e','i','o','u','A','E','I','O','U']:
        count=count+1
print("No of Vovels in a string:",count)
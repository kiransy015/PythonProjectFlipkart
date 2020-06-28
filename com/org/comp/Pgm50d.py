# wap to count indivual VOVELS

str = "python and selenium automation"
d = {}
for s in str:
    if s in ['a','e','i','o','u','A','E','I','O','U']:
        if s in d:
            cnt = d.get(s)
            cnt=cnt+1
            d.update({s:cnt})
        else:
            d.update({s:1})
print(d)

# splitting a string
str="1223456 status terminated India 12.8\n" \
    "1223457 status terminated India 12.8\n" \
    "1223458 status terminated India 12.8"

s = str.split("\n")

for i in range(0,len(s),1):
    if "1223457" in s[i]:
        st=s[i].replace('terminated','active')
        s[i]=st
print(s)
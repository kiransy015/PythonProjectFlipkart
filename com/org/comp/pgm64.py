# File Handling
# Reading data from text file

file = open("G:\Kiran\Python\data.txt")
data = file.read()
print(data)

# To fetch/get specific no of characters from a file
file = open("G:\Kiran\Python\data.txt")
data = file.read(10)
print(data)

# Reading content of first line in a text file
file = open("G:\Kiran\Python\data.txt")
data = file.readline()
print(data)

file = open("G:\Kiran\Python\data.txt")
data = file.readlines()
print(data)


# Writimg data to a text file
# str = 'Japan'
# file = open("G:\Kiran\Python\data.txt",mode='w')
# file.write(str)
# file.close()

# Append data to a text file
# str = "Japan"
# file = open("G:\Kiran\Python\data.txt",mode='a')
# data = file.write("\n")
# file.write(str)
# file.close()

# Reading data from json file
import json
file = open("G:\Kiran\Python\data.json")
data = json.load(file)
print(data)
print(type(data))
print(data['age'])
print(data.get('name'))
file.close()


# Writing data to json file
# import json
# info = {"age":"30","name":"Sam"}
# file = open("G:\Kiran\Python\data.json",mode='w')
# json.dump(info,file)
# file.close()

import json
info = {"age":"30","name":"Sam"}
file = open("G:\Kiran\Python\data.json")
data = json.load(file)
data.update(info)
file.close()

file = open("G:\Kiran\Python\data.json",mode='w')
json.dump(data,file)
file.close()



















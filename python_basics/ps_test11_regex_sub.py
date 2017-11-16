import re
from fileinput import input

str = "root:x:0:0:root:/root:/bin/bash"
temp = re.sub(':',"0",str)
print(str,"\n",temp)

"""If want to replace the content in original file itself, keep a backup and inplace = True, will initiate a file write - print below is necessary"""
for line in input("password.txt",backup=".bak",inplace=True):
    print(re.sub(r":","|",line)) # sub returns string with replaced content

print(str)
print(re.split(":|/",str))
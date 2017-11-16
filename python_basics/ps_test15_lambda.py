import re
power = lambda a,b: a**b # power is refernce to the lambda funct
print(power)
print(power(2,3))


items = [1,2,3,4,5,6,7,8,9]
alpha =  ['a','b','c']
temp = map(bin, items) # bin is a lambda here
print(temp)
print(list(temp))

ascii_values = map(ord, alpha)
print(list(ascii_values))

########################################
# Custom lambda function
def tag_it(arg):
    return "<ascii chr='{}'>{}</ascii>".format(chr(arg),arg)
print(tag_it(112))

#lambda eq to above def
tag_it_lambda = lambda arg:  "<ascii chr='{}'>{}</ascii>".format(chr(arg),arg)
temp = map(tag_it_lambda,items)
print(list(temp))

########################################
#power as lambda
print("\n\n Power as lambda")

def power(a,b):
    return a**b

t1 = [1,2,3,4]
t2 = [4,3,2,1]
for item in map(power, t1,t2):
    print(item)

########################################
print("\n\n divisible by 7")
items = list(range(1,100))
by_7 = filter(lambda n: n%7==0, items) # same as map, removes all False/blank values
#by_7 = filter(lambda n: n if n%7==0 else None, items)
print(list(by_7))

########################################
pattern = "root"
paths = filter(lambda line: re.search(pattern,line, re.I), open("password.txt"))
print(list(paths))

########################################
from functools import reduce

print("\n\n Sum with - reduce builtin Module")
sum = reduce(lambda a,b: a+b, items)
print(sum)

print()
def sum_it(a,b):
    print(a,b)
    return a+b
print(reduce(sum_it, items))
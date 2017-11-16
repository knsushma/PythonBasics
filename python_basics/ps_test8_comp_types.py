from pprint import pprint as pp

# Initializing a list
print("LIST Operations")
t = list()  # []
t = [2, 4, 6]

# 4 basic operations - append, insert , pop, remove
t.append(12)
t.insert(0, 32)
t.pop()  # del by index (by default deletes last item) t.pop(-1)
t.remove(32)  # del by value
print(t)

# extend operation
t.extend("aeiou")  # adds each ch as new item to list
print(t)
temp = ["aeiou", "try"]
t.extend(temp)
print(t)

# split to tokenize the string
x = "To infinity and beyond! We're getting close"
print(x.split(" "))
print(x.split(" ")[2:])  # slicing

# using enumerator
enu = enumerate(t)
print(enu)  #

for index, value in enumerate(x):
    print("[{}] -> {}".format(index, value))

# list comprehention
temp = [1, 2, 3, 4, 5, 6, 7, 8, 9]
t = [hex(item) for item in temp]
print(t)
t = [i ** i for i in temp]
print(t)
t = [i for i in temp if i % 2]
print(t)

users = [line.split(":")[0] for line in open("password.txt")]
print(users)
users = sorted([line.split(":")[0] for line in open("password.txt") if line.startswith("a")])  # start of the line
print(users)
users = [line.split(":")[0] for line in open("password.txt") if line.endswith("n")]  # end of line
print(users)

# sort - saves the sorted items in same object, doesn't return object. returns None
# sorted() - returns object after sorting

# Zipping
t1 = ["Name", "Age"]
t2 = ["Sushma", "24"]
merge = (zip(t1, t2))

# Matrixs
print("\nMatrix Operations")
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(matrix[1][1])

for row in matrix:
    for col in row:
        print(col, end="\t")
    print()

# parse the file to output data in matrix fashion
try:
    fp = open("password.txt")
    row = [line.split(":") for line in fp]
    # row = [line.rstrip().split(":") for line in fp] #rstrip()
    # row = [line.split(":") for line in fp if line.rstrip()] # unless empty
    print(type(row))
    for r in row:
        for c in r:
            print(c, end="\t")
        print()

except Exception as e:
    print(e)

print("\n\n")
# Dictionary - fromkeys, get, items, keys, pop, popitem, setdefault, update, values
# for lookup which provides faster search unlike in arrays
d = dict()  # {}
print(d)
print(type(d))
print(len(d))

dic = {"1": ["one","one"], "2": "two", "2": "three", "4" : {"4":"four"}}
print(dic)

# add, update, delete, read aka update, iteration
# add
dic["3"] = "three"
print(dic)

# update
if "2" in dic:
    dic["2"] = "two"
print(dic)

# read
print(dic["1"])
# dic["22"] # error
print(dic.get("22"))  # None

# #delete
# dic.pop("2")
# dic.popitem() # randomly deletes an item

# iteration
print("\n\n Iterations")
for key, value in dic.items():
    print("{} => {}".format(key, value))

for key, value in dic.items():
    print(key, end="=>")
    if type(value) is list:
        for v in value:
            print("\t",v)
    elif type(value) is dict:
        for k,v in value.items():
            print("\t",k, ":", v)
    else:
        print(value)

# dictionary comprehention
print("Dictionary Comp")
items = [{i: [bin(i)]} for i in range(1, 10)]
pp(items)


print("\n\n")
print("SET Operations")
a = [1,2,3,4,5]
b = [1,5,7,3,9]

x = set(a)
y = set(b)

print(list(x.intersection(y)))
print(x & y)
print(list(x.union(y)))
print(x | y)
print(list(x.difference(y)))
print(x-y)


#Tuples
t = tuple() # ()
print(type(t))
t = (1,"sush",3,9)

print(t[-2])
print(t[:-1])

for i in t:
    print(t)

# Passing tuples as arguments - content of tuple
def compute(a,b,c):
    print("multiple:{}".format(a*b*c))

t = (23,30,40)
compute(*t) # *t is content of tuple (applicable to even list)
#compute(*t) is equivalent to compute(t[0], t[1], t[2])
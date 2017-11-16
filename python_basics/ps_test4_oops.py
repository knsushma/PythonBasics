import sys
class Demo:
    pass # dummy code black, required as class is a compound statement, should have a single statement atleast

d = Demo()
print(d)
print(type(d))
print(__name__) # default namespace of script as well as module
print(sys.__name__)
print("class end")
print()

class Demo1:
    def __init__(self):
        print("I am a constructor")

    def __del__(self):
        print("I am a destructor")

d = Demo1()

# this - no this keyword
# self - to refer to current obj , can define any name

class PackageManager:
    def __init__(self, name=None, version=None): # None(NoneType) - as default const is not supported - no method overloading
        self.name = name
        self.version = version

    def __del__(self):
        print("object destroyed")

    def get_information(self):
        print("Name: ", self.name)
        print("Version:", self.version)

p = PackageManager()
p.get_information()
p1 = PackageManager("pip","9.1")
p1.get_information()
PackageManager("java", "7").get_information()
PackageManager.get_information(p1)



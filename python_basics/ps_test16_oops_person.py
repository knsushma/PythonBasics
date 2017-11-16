#shallow copy - shares the same memory loc (for efficient use of memory)
#deep copy - cloning an object (take a copy of that object)
from copy import deepcopy # deepcopy for class objects, copy() - for variables
class Person:
    def __init__(self,f_name,l_name):
       self.first_name = f_name
       self.last_name = l_name
       #print("Type:",self)

    def get_info(self):
        print("First Name:",self.first_name)
        print("Last Name:",self.last_name)


if __name__ == '__main__':
    p = Person('Sushma', "K N")
    print("\nP object:")
    p.get_info()
    p2 = p # shallow copy
    print("\nShallowed copied from p: ")
    p2.get_info()
    p3 = deepcopy(p) # deep copy
    p3.first_name = "Sush"
    print("\nDeep Copied from p: ")
    p3.get_info()

class Box:
    def __init__(self,size):
        self.size = size

    def __add__(self, other):
        return (Box(self.size + other.size))

    def __mul__(self, other):
        return (Box(self.size*3))

    # print will get the string form of an object, Now print the class name with value for size
    def __str__(self):
        return ("[{} Size : {}]".format(self.__class__.__name__,self.size))


if __name__ == '__main__':
    b1 = Box(2)
    b2 = Box(3)
    b3 = b1 + b2 # b1.__add(b2)
    print(b3)
    print("\nMultiplied sized with 3:",b3*3) # b3.__mul(3)

########################################
from io import FileIO
from collections import deque


class CustomFileIO(FileIO):
    def __lshift__(self, other):
        content = b''
        self.seek(0, 0)

        while other:
            content += self.readline()
            other -= 1

    def __rshift__(self, other):
        self.seek(0, 0)
        content = b''.join(deque(self,other))
        return content.decode("ascii")

if __name__ == '__main__':
    cf = CustomFileIO("password.txt")
    print(cf >> 2)  ## t print last 2 lines
    print()
    print(cf << 2)  # to print first 2 lines

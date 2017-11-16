class PackageManager:
    def __init__(self, name=None, version=None): # None(NoneType) - as default const is not supported - no method overloading
        self.__name = name
        self.version = version

    def __del__(self):
        print("object destroyed")

    def __get_information(self):
        print("Name: ", self.__name)
        print("Version:", self.version)

    def wrapper(self):
        self.__get_information()

p = PackageManager("pip","9.0")
p.wrapper()
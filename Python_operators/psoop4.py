class PackageManager:
    def __init__(self, name=None, version=None):
        self.__name = name
        self.version = version

    def __get_information(self):
        print('name :', self.__name)
        print('version :', self.version)

    def wrapper(self):
        self.__get_information()


pm = PackageManager('pip', 2.2)
pm.wrapper()
print()
# print(pm.__name)

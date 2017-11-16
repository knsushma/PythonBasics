class PackageManager:
    def __init__(self, name=None, version=None):
        self.name = name
        self.version = version

    def get_information(self):
        print('name :', self.name)
        print('version :', self.version)


pm = PackageManager('pip', 2.2)
pm.get_information()
print()
print(pm.name)
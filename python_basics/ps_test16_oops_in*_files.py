from os import listdir, stat
from os.path import join, isfile, basename # from absolute path => basename - to get filename, dir - to get dir_name
from time import ctime
from pprint import pprint as pp
# fs = stat("/etc/resolv.conf")
# print(fs)
# print(fs.st_size)
# print(ctime(fs.st_mtime))

# Get File metadata under mentioned directories
class DirStatistics:
    def __init__(self,*args):
        self.directory_names = args
        print(self.directory_names)
        self.container = dict()
        self.__get_file_statistics()

    def __get_file_statistics(self):
        for dir in self.directory_names:
            dir_names = [join(dir,item) for item in listdir(dir)]
            file_names = filter(isfile, dir_names)
            for file_name in file_names:
                fs = stat(file_name)
                #file_name = basename(file_name)
                #syntax : d.setdefault(k1,{})[k2] = {k3:v....} # can have any level of nesting
                self.container.setdefault(dir,{})[basename(file_name)] = [fs.st_size, fs.st_mtime]

if __name__ == '__main__':
    d = DirStatistics("/etc")
    pp(d.container)

#########################################
# dump file_statistics into json file
from json import dump

class DirListing2JSON(DirStatistics):
    def dump_json_data(self,json_file):
        try:
            dump(self.container, open(json_file,"w"),indent=4)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    DirListing2JSON("/etc","/tmp").dump_json_data("file_statistics.json")

#########################################
#Read a JSON file
from json import load, loads #load - read from file, loads - read from dict_variable
content = load(open("file_statistics.json"))
pp(content)

for dir_name, dir_items in content.items():
    for file_name, file_prop in dir_items.items():
        print("\t",file_name)

        for name, value in zip(["Size","mtime"],file_prop):
            print("\t\t",name,":",value)

        print()

#########################################
#To walk through a directory
from os import walk
for root, dir_name,files in walk("/home/"):
    pdfs = list(filter(lambda dn: dn.endswith(".pdf"), files))

    if pdfs:
        print("\t", root)
        for pdf in pdfs:
            print("\t\t",pdf )
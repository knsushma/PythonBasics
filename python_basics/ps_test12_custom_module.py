from pprint import pprint as pp
from os import listdir
from os.path import join, isdir, isfile

class ReadDir:
    def get_files_under_directory(self,dir_name):
        dirs = [join(dir_name,item) for item in listdir(dir_name)]
        file_names = [item for item in dirs if isfile(item) ]
        return file_names

if __name__ == '__main__':
    print(__name__)
    pp(ReadDir().get_files_under_directory("/etc"))
    print
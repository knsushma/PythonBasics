#to read specific line form file
from fileinput import input, filelineno
from pprint import pprint as pp
print("Specific line from a file")
for line in input("password.txt"):
    if filelineno() == 15 and line.rstrip():
        print("{} => {}".format(filelineno(),line))

# Read and Write to a file
try:
    fp = open('password.txt')#default opens it in read mode
    for line in fp:
        #print(line)
        print(line,end='')
    fp.close()
except Exception as e:
    print(e)
finally:
    fp.close()

print()
try:
    fp = open('password.txt',"r")
    users = list()
    for line in fp:
        users.append(line.split(":")[0])
    users.sort()
    for index,user in enumerate(users, 1): # enumerator by default starts indexing from 0, possible to specify index also
        print(index,user)
    fp.close()
except Exception as e:
    print(e)
finally:
    fp.close()


# with class - same prb as above
class UserList:
    def __init__(self,data_file,target_file):
        self.data_file = data_file
        self.target_file = target_file
        self.user_list = list()
        self.__parse_data_file()

    def __parse_data_file(self):
        try:
            fp = open(self.data_file)
            for line in fp:
                self.user_list.append(line.split(":")[0])
            self.user_list.sort()
        except Exception as e:
            print(e)
        finally:
            fp.close()

    def get_users(self):
        fw = open(self.target_file, "r+")
        for index, name in enumerate(self.user_list):
            print("[{}] -> {}".format(index, name))
            fw.write(name + "\n")
        fw.close()

l = UserList('password.txt',"password1.txt")
l.get_users()


#Zipping
tags  = [1,2,3,4,5,6,7]
try:
    fp = open("password.txt")
    content = [line.split(":") for line in fp ]
    #row = [line.rstrip().split(":") for line in fp] #rstrip()
    for data in content:
        for index, value in zip(tags,data):
            #print(index, "=>", value)
            print("{:>12} : {}".format(index,value))
except Exception as e:
    print(e)
finally:
    fp.close()


from glob import glob
print(glob("/etc/pass*")) # list all file under directory
from os import listdir
from os.path import join, isdir, isfile

dir_name = "/etc"
print(listdir(dir_name))
#pp(dir_name + "//" + "password.txt")
pp([join(dir_name, item) for item in listdir(dir_name)])
print("\n\n\n")

def get_files_under_directory(dir_name):
    dirs = [join(dir_name,item) for item in listdir(dir_name)]
    file_names = [item for item in dirs if isfile(item) ]
    pp(file_names)
get_files_under_directory("/etc")
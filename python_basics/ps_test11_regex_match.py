import re
import ps_test12_custom_module
from fileinput import filelineno, filename, input
from pprint import pprint as pp
# To get matched and unmatched substring using regular expressions
s = "The python and the perl scripting"
pattern = "P.+N" # greedy match - Atmost ch are considered
pattern = "P.+?N" # non-greedy match - shortest ch is considered


m = re.search(pattern, s, re.I) # third agr to ignore case sensitive
if m:
    print(m)
    print("Match:", m.group())
    print(m.start()) # starting index of matched substring
    print(m.end()) # ending index of the matched substring
    print(m.span()) # start and end index
    before = s[:m.start()]
    after = s[m.end():]
    print("before:", before)
    print("after:",after)
else:
    print("Failed to match")


# Finding multiple matches in the same line
for m in re.finditer(pattern, s, re.I):
    print(m.group)
    print(m.span())
    print()

print(re.findall(pattern,s,re.I))


# read content from a file , match for a substring and print the whole line with line no if the match is found

class MatchSubstring:
    def __init__(self,regex,*args):
        self.regex = regex
        self.file_names = args
        self.__grep_substring()

    def __grep_substring(self):
        try:
            for line in input(self.file_names):
                if re.search(self.regex,line,re.I):
                  print("{}: {} : {} ".format(filename(), filelineno(), line))
        except Exception as e:
            print(e)
        finally:
            pass
MatchSubstring("root","/etc/passwd","/etc/group")
print("\n\n\n Usinf Custom Module to find files")
filenames = ps_test12_custom_module.ReadDir().get_files_under_directory(".")
#pp(len(filenames))
#filenames = [item for item in filenames if item.endswith("py")]
#pp(filenames)
pp(len(filenames))
MatchSubstring("test",*filenames) # *filenames -> content of filenames(a list)

from collections import deque

#Get last 5 lines of a file
for line in deque(open("password.txt"),5): # deque(data, num_of_lines)
    print(line)

for line_no, line in enumerate(open("password.txt"),1):
    if line_no == 15 and line.rstrip():
        print("\nSpecific line: {} =>{}".format(line_no,line))
s = 'this is a sample string in python'

for item in s:
    if item not in 'aeiou ':  # membership test operator
        print("{} : {}".format(item, ord(item)))
    else:
        print('**')
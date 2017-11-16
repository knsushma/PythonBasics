""" demo for string formatting """

name, age, gender = 'sushma', 24, 'female'

print('{}|{}|{}'.format(name,age,gender))
print('{:>20}|{:>15}|{:>10}'.format(name,age,gender)) # max of 20 characters, will be right justified
print('{:<20}|{:<15}|{:<10}'.format(name,age,gender)) # min of 20 characters, will be left justified
print('{:^20}|{:^15}|{:^10}'.format(name,age,gender)) # min of 20 characters, will be center justified
print('{:20}|{:15}|{:10}'.format(name,age,gender)) # min of 20 characters, will be default center


import pprint
try:
    name = 'sushma'
    city = 'bangalore'

    print('name:', name)
    print('city:', city)

    # name = input("enter the name:")
    # print(name)
    # age = int(input("enter age:"))
    # print(age)
    zip_code = int(input("enter your city ZIP code"))
    print(zip_code)
except Exception as err:
    print(err)
finally:
    print("finally block of the exception handling")

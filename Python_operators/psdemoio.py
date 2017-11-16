try:
    name = input('enter the name :')
    city = input('enter the city :')
    zip_code = int(input('enter the postal zipcode :')) / 0

    print('name :', name)
    print('city :', city)
    print(zip_code)
    print(type(zip_code))
except ValueError as err:
    print(err)
except Exception as err:
    print('internal script error')
    print(err)
    print(type(err))
finally:
    print('finally block of the exception handling')

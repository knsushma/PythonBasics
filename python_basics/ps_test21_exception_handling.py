def safe_print(value):
    try:
        print(float(value)/0)
    except ValueError as err:
        print(err)
    except (KeyError, IndexError) as err:
        print(err)
    except Exception as err:
        print(err)
    finally:
        print("finally block from exception handling")

safe_print("fdv")

##############################
#Railsing custom exception
class RangeError(Exception):
    def __str__(self):
        return "{}:{}".format(self.__class__.__name__,self.args[0])

def check_4_range(value):
    if value not in list(range(50,100)):
        raise RangeError("\nvalue not in the range : {}".format(value))
    return True

if __name__ == '__main__':
    try:
        check_4_range(100)
    except RangeError as err:
        print(err)


##############################
#Using Assertion

def power(a,b):
    return a**b

try:
    assert power(2,3)==8, "failed"
except AssertionError as err:
    print(err)

try:
    assert power(2,3)==18, "failed"
except AssertionError as err:
    print(err)

power(2,3)
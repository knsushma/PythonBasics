def power(m,n): #fixed or positional argument function
    return (m ** n)

def power1(m,n=1): # default arguments preceeds from right to left <-
    return (m ** n)

print(power(2,3))
print(power1(3))
print("\n\n")

# *args -> variable length parameter
# **args -> keyword parameter
def demo(**args):
    print(args)

demo()
demo(name="Sushma", age=24)


# problem
def cat_tac_rev(filename,**args):
    reverse = args.get('reverse')
    mirror = args.get('mirror')

    content = open(filename).readlines()

    if reverse:
        content.reverse()
    if mirror:
        content = [line[::-1] for line in content]

    return ''.join(content)

print(cat_tac_rev("/etc/resolv.conf"))
print(cat_tac_rev("/etc/resolv.conf", reverse=True, mirror=False))
print(cat_tac_rev("/etc/resolv.conf", reverse=True, mirror=True))

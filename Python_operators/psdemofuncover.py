import socketserver
help(socketserver.ThreadingTCPServer)


def demo():
    print("null argument function")

print(demo)

def demo(a, b):
    print(a + b)


print(demo)
print(type(demo))

n = 12
n = 12.21
demo = 'peter'
print(demo)
print(type(demo))

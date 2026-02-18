import random
name = "dominic"
def test():
    x = 1
    y = 2
    return x, y, 3

def hello():
    print(f"hello {name}")

def main():
    global name
    name = "john"
    print(f"hello {name}")
    hello()
    print(random.randint(0, 6))
    a, b, c = test()
    print(a)
    print(b)
    print(c)
main()
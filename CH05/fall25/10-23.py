def hello(name):
    print(f"Hello {name}!")

def add_one(x):
    x += 1
    return x

def print_x():
    print(f"x is {x}")

def update_x():
    global x 
    x = 4

def main():
    # y = hello("Jason")
    # print(y)
    # x = "Dominic"
    # hello(x)
    
    print_x()
    update_x()
    print_x()

x = 10
main()
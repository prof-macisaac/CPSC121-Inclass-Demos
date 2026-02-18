VERSION = 3

total = 1
def hello(name, greeting):
    hello_str = f"{greeting} {name}"
    print(hello_str)
    # return hello_str

def sum(a, b):
    c = a + b
    total = 2
    print(f"total in sum: {total}")
    return c, a


def main():
    # hello("dom")
    
    total_dice,avg_dice = sum(int(input("enter val 1: ")),int(input("enter val 2: ")))
    print(x)
    print(y)
    print(f"total in main: {total}")
    # name = "chiana"
    # print(f"hello {name}")
    # hello()

    # global name
    # name = "chiana"
    # print(f"hello {name}")
    # hello()

main()
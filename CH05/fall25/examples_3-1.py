import random
name = "dominic"

def hello():
    name = "max"
    print(f"hello {name} from hello")
def random_testing():
    random.seed(1)
    weather = random.randint(1,6)
    print(f"the value is {random.randint(1,6)}")
    print(f"the value is {random.randint(1,6)}")
    rand_float = random.random()
    print(f"the random float is {rand_float}")
    rand_float_2 = random.uniform(2.5, 3.7)
    print(f"the random float is {rand_float_2}")

def mult_return():
    x = 3
    y = 7
    return x, y, "three"

def main():
    global name
    name = "chiana"
    print(f"hello {name} from main")
    # hello()
    # print(f"hello {name} from main")
    random_testing()
    a, b, c = mult_return()
    print(f"a is {a} and b is {b} and c is {c}")

main()
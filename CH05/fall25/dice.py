import random
def d6():
    return random.randint(1,6)

def d4():
    return random.randint(1,4)


if __name__ == "__main__":
    d4()
    print("testing inside dice file")
# else:
#     print(__name__)
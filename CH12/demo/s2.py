def recursion():
    print("hello")
    recursion()
    return

# recursion()

# recursion()
def fact(num):
    print(f"fact({num}): begin")
    if num == 1:
        print(f"fact({num}): returning 1")

        return 1
    else:
        print(f"fact({num}): calling fact({num-1})")

        fact_return = fact(num-1)

        print(f"fact({num}): returning {num} * fact({num-1})<{fact_return}> = {num * fact_return} ")

        return num * fact_return

print(fact(5))
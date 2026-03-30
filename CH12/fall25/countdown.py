
# def recursion():
#     print("hello")
#     recursion()
#     return

# recursion()

# def hello_n_times(n):
#     if n == 0:
#         return
#     else:
#         print("hello")
#         hello_n_times(n-1)
#         return

# hello_n_times(4)

# def countdown(n):
#     if n == 0:
#         # Base case: stop when n reaches 0
#         print("Blast off!")
#         return
#     else:
#         # Recursive case: print n and call countdown on a smaller value
#         print(n)
#         countdown(n - 1)
#         return
# countdown(10)
def sum_to_n(num):
    if num == 1:
        return 1

    return num + sum_to_n(num - 1)

print(sum_to_n(3))



def factorial(num):
    if num == 1:
        return 1

    return num * factorial(num-1)
    
# print(factorial(3))

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

# print(fact(5))
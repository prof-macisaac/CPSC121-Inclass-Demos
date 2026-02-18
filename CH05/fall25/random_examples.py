# import statement at top of the file
import random
import dice
# import modules.dice as dice

# we can set the seed for random to a specific value for consistent testing between runs (this ensures that all subsequent random calls are based on this number. They will be the same every time we run the program)
# random.seed()

# this range INCLUDES 0 and 10
# secret_number = random.randint(0,10)
# print(secret_number)
# print(random.randint(0,10))
# print(random.randint(0,10))
# print(random.randint(0,10))


# print(random.random())

# print(random.uniform(2.5, 3.5))

print(dice.d6())

# print(__name__)
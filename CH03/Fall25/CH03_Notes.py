

# # Example if statement
# if 1 == 1:
#     print("1 equals 1, so this prints!")
#     print("we can do multiple things in here")

# if 1 == 2:
#     print("This will not print, as 1 does not equal 2")
#     print("we can do multiple things in here")

# # Using variables

a = 10
b = 10
# if b > a:
#     print("the value in b is greater than the value in a, so this prints")
#     print("we can put many statements within a block")
# # print("this will print always")

# if a > b:
#     print("a is currently smaller than b, so this doesn't print")

if a != b:
    print("a does not equal b, so this prints out!")

# a = 10

# if a == b:
#     print("now a and b are equal, so this prints outs")

# if a <= b:
#     print("a is less than or equal to (in this case equal to) b, so this prints")

# a = 9
# if a <= b:
#     print("a is less than or equal to (in this case less than) b, so this prints")
# if a >=8:
#     print(a," is greater than or equal to", 8)


# Else statements evaluate when the if statement is false

# x = 100
# y = 200
# if x > y:
#     print(x, "is bigger than", y)
# else:
#     print(x, "is not bigger than", y)
#     x = x + y
#     print("x is now", x)

# if x > y:
#     print(x, "is bigger than", y)


"""
================= Class Task =================
#1. Write a program that takes a temperature as input, and if temp is greater than a certain temperature (you can choose the temp), it says it's hot out, if not greater than that point, it says it's not hot.
- Hint! Make sure to change the string input into a float/int
"""
# HIGH_TEMP = 80
# current_temp = float(input("What is the current temperature (F): "))
# if current_temp >= HIGH_TEMP:
#     print("Its hot out!")
# else:
#     print("Its not very hot out")






# Answer
# temp = int(input("What is the temperature? "))
# if temp >= 80:
#     print("It's hot out")
# else:
#     print("It's not very hot out")

# single line if statements

# if True: print("Since we are only doing a" +
#         "single thing in this if statement," +
#         " we can put it on a single line.")

# Comparing strings
# Mostly will use == or !=, but you can compare strings with all comparison operators

# user_decision = input("do you agree? ")
# if user_decision == "yes":
#     print("The user agreed")

# mary = "Mary"
# mark = "Mark"
# if mary > mark:
#     print("the name", mary, "has a larger ASCII value than", mark)
# else:
#     print("the name", mark, "has a larger or equal ASCII value than", mary)




# if-elif-else Statements

burgers_eaten_today = -2
if burgers_eaten_today < 1:
    print("Get this guy a burger!")
elif burgers_eaten_today == 1:
    print("a treat")
elif burgers_eaten_today == 1:
    print("a respectable amount of burgers")
else:
    print("dang, thats alot of burgers")

# It will only evaluate the first one that is true!

x = 4
if x < 4:
    print(x, "less than 4")
elif x <= 4:
    print(x, "less than/equal to 4")
elif x == 4:
    print(x, " is 4")
elif x >= 4:
    print(x, "greater than/equal to 4")
elif x > 4:
    print(x, "greater than 4")


# # Nested If Statements


dogs_count = 5
result = ""

if dogs_count > 0:
    print("glad you have atleast 1 dog")
    result = "good amount of dogs"
    if dogs_count > 3:
        result = "thats a lot of dogs"
    else:
        print("great amount of dogs")
else:
    result= "get a dog"

print(result)


"""
And and Or Operators!

Used for combining logic

Combos:
    false and false: false
    false or false: false

    false and true: false
    false or true: true

    true and false: false
    true or false: true

    true and true: true
    true or true: true

Basic Rule: 
    AND requires both expressions to be true
    OR requires only a single expression to be true

"""

income = 80000
household_size = 3

if income < 100000 and household_size > 2:
    print("Qualified for financial aid")
else:
    print("Not qualified for financial aid")
# parentheses are helpful to distinguish the two expressions, but aren't required
if (income < 100000) and (household_size > 2):
    print("Qualified!")


salads_eaten = 2
veggies_eaten=  1
if salads_eaten > 4 or veggies_eaten > 4:
    print("good work getting nutrients!")
else:
    print("eat more greens!")


"""
================= Class Task =================
#2. Write a program that asks the user for their age (int) and if they are a student (y or n). 

- Ages under 5 and 65 or older get free admission, 
- if they are over 13 and a student, they get the student discount
- otherwise, they pay regular price
print out which admission they must pay
"""



"""
================= Not Operator =================
not operator goes before an boolean expression and reverses its value

true -> false
false -> true

ex:
x = 1
if not x == 1:
    print("x is not 1")
explanation: it first checks if x equals 1.
            if it does, the value is True, the not operator then converts this to False

            if it does not, the value is False, the not operator then converts this to True
"""

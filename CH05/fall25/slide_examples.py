
# both these functions (print_next_number and get_previous_number) have the local variable 'num' but these are separate variables contained to just their respective functions

def get_previous_number(num):
    prev_num = num - 1
    return prev_num

def not_written_yet():
    pass

def sum_some_nums(a, b, multiplier=1, additional_val=0):
    result = (a + b + additional_val) * multiplier
    print(result)

def print_next_number(num):
    next_number = num + 1
    print(f"the next number is {next_number}")

print_next_number(8)

def main():
    # not_written_yet()
    x = 5
    # # passing x into our newly created function
    print_next_number(x)
    # print(f"x is still {x}")
    # # not_written_yet()
    print_next_number(7)
    sum_some_nums(2,3, multiplier=4)

    # I can call this function but nothing will happen
    

    #####################
    # next_number is a local variable!
    # so if we try to access it outside of that function
    # it gives an error
    
    #print(f"the next number is {next_number}")

    #####################
    # num is also a local variable so we don't have access to that outside of the function
    
    # print(f"the number is {num}")

    #####################
    # functions can return things as well
    # in this case, get_previous_number will return a number
    # we can save this value into a variable
    
    # prev = get_previous_number(x)
    # print(f"the previous number is {prev}")
    #####################

    # when we call get_previous_number with x, we send a copy of x to the function. x remains unchanged to us
    # this is called pass by value
    # print(f"x is still {x}")

main()
# example of why you might use finally instead
# of just having code after the finally block

def error_function():
    # we're going to create an error on purpose here
    # to demonstrate the finally block
    try:
        if True: #set to false to not get the error
            not_good = 1/0 #div by zero        
    except ZeroDivisionError as err:
        print(f"We divided by zero... ({err})")
        return False


    print("we won't hit this line of code")

def main():
    error_function()

if __name__ == "__main__":
    main()
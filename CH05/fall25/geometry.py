import math
import random
def calc_circle(radius):
    area = calc_circle_area(radius)
    circumference = calc_circle_circumference(radius)
    return area, circumference

def calc_circle_circumference(radius):
    return math.pi * radius * 2

def calc_circle_area(radius):
    return math.pi * (radius ** 2)

def calc_rectangle(height, width):
    area = calc_rectangle_area(height,width)
    perimeter = calc_rectangle_perimeter(height,width)
    return area, perimeter

def calc_rectangle_area(height, width):
    return height * width

def calc_rectangle_perimeter(height, width):
    return 2 * height + 2 * width

def show_menu(check_random=True):
    
    choice  = input("""Which shape would you like the area and perimeter of? 
    a) circle
    b) rectangle
    c) square
""")
    if check_random:
        random_size = input("Would you like the size to be random (yes/no)? ") == "yes"
    else:
        random_size = False
    return choice, random_size

def main():
    choice, random_size = show_menu(check_random=False)

    if choice == "a":
        # circle
        if random_size:
            radius = random.randint(1,100)
            print(f"the random radius is {radius}")
        else:
            radius = float(input("What is the radius of the circle? "))
        area, circumference = calc_circle(radius)
        print(f"your circle has an area of {area:.4f} and a circumference of {circumference:.4f}")
    elif choice == "b":
        # rectangle
        height = float(input("What is the height of the rectangle? "))
        width = float(input("What is the width of the rectangle? "))
        area, perimeter = calc_rectangle(height, width)
        print(f"your rectangle has an area of {area:.4f} and a perimeter of {perimeter:.4f}")
    elif choice == "c":
        # square
        width = float(input("What is the width of the square? "))
        area, perimeter = calc_rectangle(width, width)
        print(f"your square has an area of {area:.4f} and a perimeter of {perimeter:.4f}")
    else:
        print("That is not a valid option.")
    
    print("Goodbye now!")

main()

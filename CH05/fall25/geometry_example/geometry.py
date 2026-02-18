import geometry_helper
def show_menu():
    shape = input("""What shape would you like to do calculations with? 
a) circle
b) rectangle
c) square
""")
    return shape

def get_num(prompt):
    num = float(input(prompt))
    return num

def main():
    response = show_menu()
    if response == "a":
        # circle
        radius = get_num("What is the radius of the circle? ")
        cir, area = geometry_helper.calc_circle(radius)
        print(f"the area of the circle is {area:.4f} and the circumference is {cir:.4f}")
    elif response == "b":
        length = get_num("What is the length of the rectangle? ")
        width = get_num("What is the width of the rectangle? ")
        perimeter, area = geometry_helper.calc_rectangle(length, width)
        print(f"the area is {area} and the perimeter is {perimeter}")
    else:
        length = get_num("What is the length of the square? ")
        perimeter, area = geometry_helper.calc_rectangle(length)
        print(f"the area is {area} and the perimeter is {perimeter}")


if __name__ == "__main__":
    main()
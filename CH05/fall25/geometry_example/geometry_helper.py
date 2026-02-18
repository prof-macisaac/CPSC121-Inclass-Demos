import math

def calc_circle(radius):
    circumference = math.pi * 2 * radius
    area = math.pi * (radius ** 2)
    return circumference, area

def calc_rectangle(length, width = None):
    if width == None:
        width = length
    perimeter = 2 * length + 2 * width
    area = length * width
    return perimeter, area

def main():
    print(calc_circle(1))

if __name__ == "__main__":
    print(__name__)
    main()
else:
    print(__name__)
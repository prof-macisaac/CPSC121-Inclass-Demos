
class Car():
    def __init__(self, brand, year, miles):
        self.brand = brand
        self.year = year
        self.__miles = miles
    
    def get_brand(self):
        return self.brand

    def get_miles(self):
        return self.__miles
    
    def set_brand(self, new_brand):
        self.brand = new_brand

    def add_miles(self, added_miles):
        if added_miles < 0:
            print("That is not allowed")
        else:
            self.__miles += added_miles

    def __str__(self):
        string = f'{self.brand} {self.year} {self.__miles}'
        string2 = "car"
        return string2
    
    def get_year(self):
        return self.year
    def set_year(self, new_year):
        self.year = new_year

def add_1_to_year(car):
    year = car.get_year()
    car.set_year(year+1)

def main():
    volvo = Car("Volvo", 2008, 195000)
    add_1_to_year(volvo)

    # volvo.set_brand("Lexus")
    volvo.add_miles(1000)
    volvo.__miles = 0
    print(f"hello")
    print(volvo.get_miles())
    print(volvo.get_brand())

    toyota = Car("Toyota", 2026, 0)

    print(toyota.year)



    cars = [volvo]
    cars.append(toyota)
    # print(cars[0])
    # cars.append(toyota)
    # print(cars[1])

    # print(volvo)
    for car in cars:
        print(car)
        car.get_miles()
        car.add_miles(5)
        print(car)



main()
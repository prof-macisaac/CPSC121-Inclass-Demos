class Car():
    def __init__(self, brand, year, miles):
        self.brand = brand
        self.year = year
        self.__miles = miles

    def get_brand(self):
        return self.brand
    def get_year(self):
        return self.year

    def set_brand(self,new_brand):
        self.brand = new_brand

    def get_miles(self):
        return self.__miles

    def set_miles(self, new_miles):
        self.__miles += new_miles

    def __str__(self):
        return_string = f'Car: {self.brand} {self.year}, miles: {self.__miles}'
        return return_string

def add_miles(car, miles_added):
    original_miles = car.get_miles()

    car.set_miles(original_miles+miles_added)

def main():
    volvo = Car("Volvo", 2008, 195000)
    volvo.set_brand("Lexus")
    print(volvo.get_brand())
    # toyota = Car()

    cars = [volvo]
    toyota = Car("Toyota", 2026, 0)
    volvo.__miles = 10
    add_miles(volvo, 200)
    print(volvo.get_miles())
    # cars.append(toyota)
    # for car in cars:
    #     car.set_brand("Ford")
    #     print(car)

main()
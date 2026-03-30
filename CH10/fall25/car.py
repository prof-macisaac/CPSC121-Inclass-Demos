
class Car:
    def __init__(self, x, year, miles=0):
        self.__brand = x
        self.__year = year
        self.__miles = miles
    
    def get_miles(self):
        return self.__miles

    def set_miles(self, new_miles):
        self.__miles = new_miles

    def get_brand(self):
        return self.__brand
    
    def set_brand(self, new_brand):
        self.__brand = new_brand
    

    

def main():
    volvo = Car("Volvo", 2026)
    toyota = Car("Toyota", 2008, 195000)
    print(volvo.get_miles())
    volvo.set_miles(20)
    print(volvo.get_miles())
    # print(toyota.miles)
    toyota.miles = 0

main()
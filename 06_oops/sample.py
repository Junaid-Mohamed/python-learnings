class Car:
    # brand = None
    # model = None
    # can be done like this aswell but we do it with constructor __init__ method

    # class variables
    total_cars = 0
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
        self.total_cars += 1 # can be done like this but we can do it directly by accessing the class name as well
        Car.total_cars += 1
    
    def get_brand(self):
        return self.__brand + " !"

    def set_brand(self,brand):
        self.__brand = brand
    
    def fullName(self):
        return f"{self.__brand} {self.model}"

    """
    Using @property and @<property>.setter (Pythonic way):
    This is cleaner and lets you use attribute-style access while keeping control.
    """

    @property
    def brand(self):
        return self.__brand
    
    @brand.setter
    def brand(self, value):
        self.__brand = value

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod 
    def general_description():
        return "Cars are means of transport"
    
my_car = Car("Toyato", "Corolla")
# print(my_car.brand)
print(my_car.fullName())
print(my_car.get_brand())
my_car.set_brand("Maruthi")
print(my_car.get_brand())

print(my_car.brand) # access via @property
my_car.brand = "Honda" # set via @brand.setter
print(my_car.fullName())
print(my_car.fuel_type())
print(my_car.general_description())

# access class variable through object or class

print(my_car.total_cars)

class ElectricCar(Car):

    def __init__(self,brand,model,batterySize):
        super().__init__(brand,model)
        self.batterySize = batterySize

    def fuel_type(self):
        return "Electric charge"

myTesla = ElectricCar("Tesla","Model S", "85 KW")

print(myTesla.fullName())
print(myTesla.fuel_type())
print(Car.total_cars)
print(Car.general_description())

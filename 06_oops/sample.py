class Car:
    # brand = None
    # model = None
    # can be done like this aswell but we do it with constructor __init__ method

    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def fullName(self):
        return f"{self.brand} {self.model}"

my_car = Car("Toyato", "Corolla")
print(my_car.brand)
print(my_car.fullName())

class ElectricCar(Car):

    def __init__(self,brand,model,batterySize):
        super().__init__(brand,model)
        self.batterySize = batterySize

myTesla = ElectricCar("Tesla","Model S", "85 KW")

print(myTesla.fullName())
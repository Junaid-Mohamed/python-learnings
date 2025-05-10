class Car:
    # brand = None
    # model = None
    # can be done like this aswell but we do it with constructor __init__ method

    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

my_car = Car("Toyato", "Corolla")
print(my_car.brand)
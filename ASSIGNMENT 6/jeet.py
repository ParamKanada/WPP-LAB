# testfile
# class Car:
#     def __init__(self,brand, model):
#         self.brand = brand
#         self.model = model

# my_car = Car("Toyota","Corolla")
# print(my_car.brand)



class Car:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model

    def me(self):
        return f"{self.brand}{self.model}"
    
my_car = Car("TOyota","Carabolla")
    
print(my_car.me())
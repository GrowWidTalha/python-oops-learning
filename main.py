class Car:
    cars_created = 0
    def __init__(self, Brand, Model):
        self.__Brand = Brand
        self.__Model = Model
        Car.cars_created += 1
    
    def full_name(self):
        return f"The car name is {self.__Brand} {self.__Model}"

    def get_brand(self):
        return self.__Brand
    
    def fuel_type(self):
        return "This car runs on Petrol or Diesel"
    @staticmethod
    def description():
        return "This is a fuel based car"
    
    @property
    def Model(self):
        return self.__Model

# class ElectricCar(Car):
#     def __init__(self, Brand, Model, Battery_size):
#         self.Battery_size = Battery_size
#         super().__init__(self, Brand, Model)
    
#     def fuel_type(self):
#         return "This car runs on Electric charge"
        

# my_car = Car("Toyota", "Supra")
# print(my_car.Brand) # Error
# print(my_car.__Model)
# print(my_car.full_name())

# my_electric_car = ElectricCar("Tesla", "Model Y", "85KWh")
# print(my_electric_car.Brand)
# print(my_electric_car.Model)
# print(my_electric_car.Battery_size)
# print(my_electric_car.full_name())

# print(my_car.Brand) # ⛔ 
# print(my_car.get_brand()) # ✅

# print(my_car.fuel_type())
# print(my_electric_car.fuel_type())

# print(Car.cars_created)

# print(Car.description())

# print(my_car.Model)

# print(isinstance(my_electric_car, Car))
# print(isinstance(my_electric_car, ElectricCar))


class Battery: 
    def __init__(self, battery_size):
        self.battery_size = battery_size
class Engine: 
    def __init__(self, engine_power):
        self.engine_power = engine_power

class ElectricCarTwo(Car, Battery, Engine):
    def __init__(self, brand, model, battery_size, engine):
        Car.__init__(self, brand, model)
        Battery.__init__(self, battery_size)
        Engine.__init__(self, engine)
    
    def fuel_type(self):
        return "This car runs on Electric charge"
        

my_second_tesla = ElectricCarTwo("Tesla", "Model S", "45kwh", "1000hp")
print(my_second_tesla)
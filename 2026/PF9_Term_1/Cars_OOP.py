# Main - Cars_OOP
# Created by Samuel Marriott on 31/03/2026
# This is for instantiating car objects.

from car import Car

car_1 = Car("Mitsubishi", "Challenger", 2014, "white")
car_2 = Car("Mitsubishi", "ASX", 2019, "blue")
car_3 = Car("Hyundai", "i30", 2008, "cyan")

'''print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.colour)
print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.colour)'''

car_2.drive()
car_2.accelerate()
car_2.stop()
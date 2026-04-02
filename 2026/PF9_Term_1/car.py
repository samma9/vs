# Object - car
# Created by Samuel Marriott on 31/03/2026

class Car:

    def __init__(self, make, model, year, colour):
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour

    def drive(self):
        print("This "+self.model+" is driving.")
    
    def stop(self):
        print("This "+self.model+" is stopped.")

    def display_info(self):
        print(self.make, self.model, self.year, self.colour)
    
    def accelerate(self):
        print("This "+self.model+" is speeding up.")
class Vehicle:
    
    def __init__(self,make,model,year,fuel_type):
        self.make = make
        self.model = model
        self.year = year
        self.fuel_type = fuel_type
        
    def to_string(self):
        return str(self.year) + " " + self.make + " " + self.model + " - Fuel: " + self.fuel_type
from Vehicle import Vehicle

class Car(Vehicle):
    
   def __init__(self, make, model, year, fuel_type, num_doors):
      super().__init__(make, model, year, fuel_type)
      self.num_doors = num_doors
      
   def to_string(self):
      return super().to_string() + " - " + str(self.num_doors) + " doors."
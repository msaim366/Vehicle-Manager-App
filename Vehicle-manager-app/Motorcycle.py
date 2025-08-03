from Vehicle import Vehicle

class Motorcycle(Vehicle):
    
    def __init__(self, make, model, year, fuel_type, has_sidecar):
        super().__init__(make, model, year, fuel_type)
        self.has_sidecar = has_sidecar
        
    def to_string(self):
        if self.has_sidecar == True:
          return super().to_string() + " - Sidecar: Yes"
        else:
          return super().to_string() + " - Sidecar: No"
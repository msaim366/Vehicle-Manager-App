class VehicleManager:
    
    def __init__(self):
        self.vehicles = []
        
    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        
    def list_vehicles(self):
        if not self.vehicles:
            print("No Vehicles found")
        else:
            for v in self.vehicles:
                return "\n".join(v.to_string() for v in self.vehicles)
                
    def save_to_file(self, filename):
        with open(filename, "w") as f:
            for v in self.vehicles:
               f.write(v.to_string() + "\n")
               
        print("Saved " + str(len(self.vehicles)) + " vehicles to " + filename) 
        
    def load_from_file(self, filename):
        try:
            with open(filename, "r") as f:
                lines = f.readlines()
                print("Vehicles in file:")
                for line in lines:
                    print(line.strip())
                    
        except FileNotFoundError:
            print("File not found.")
from Vehicle import Vehicle
from Car import Car
from Motorcycle import Motorcycle
from vehicle_manager import VehicleManager

car1 = Car("Toyota", "Corolla", 2021, "Petrol", 4)
motorcycle1 = Motorcycle("Harley Davidson", "Street 750", 2020, "Petrol", False)

vehicle_Manager = VehicleManager()

vehicle_Manager.add_vehicle(car1)
vehicle_Manager.add_vehicle(motorcycle1)


vehicle_Manager.save_to_file("vehicles.txt")
vehicle_Manager.load_from_file("vehicles.txt")
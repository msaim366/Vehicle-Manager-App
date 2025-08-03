from Vehicle import Vehicle
from Car import Car
from Motorcycle import Motorcycle

from vehicle_manager import VehicleManager

vehicle_manager = VehicleManager()

while True:
    print("\n1. Add Car\n2. Add Motorcycle\n3. List Vehicles\n4. Save to File\n5. Load from File\n6. Exit")
    choice = input("Pick an Option: ")
    
    if choice == "1":
        make = input("Make: ")
        model = input("Model: ")
        year = int(input("Year: "))
        fuel = input("Fuel type: ")
        doors = int(input("Number of doors: "))
        car = Car(make,model,year,fuel,doors)
        vehicle_manager.add_vehicle(car)
        print("Car Added.")
        
    elif choice == "2":
       make = input("Make: ")
       model = input("Model: ")
       year = int(input("Year: ")) 
       fuel = input("Fuel type: ")
       sidecar = input("Has Sidecar? (yes/no): ").lower = "yes"
       bike = Motorcycle(make,model,year,fuel,sidecar)
       vehicle_manager.add_vehicle(bike)
       print("Motorcycle Added.")
       
    elif choice == "3":
        vehicle_manager.list_vehicles()
    elif choice == "4":
        vehicle_manager.save_to_file("vehicles.txt")
    elif choice == "5":
        vehicle_manager.load_from_file("vehicles.txt")
    elif choice == "6":
        break
    else:
        print("Invalid choice. Try again.")
    
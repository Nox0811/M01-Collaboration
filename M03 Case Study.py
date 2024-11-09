class Vehicle:
    def __init__(self):
        self.vehicle_type = None
    def set_vehicle_type(self, vehicle_type):
        self.vehicle_type = vehicle_type
class Automobile(Vehicle):
    def __init__(self):
        super().__init__()
        self.year = None
        self.make = None
        self.model = None
        self.doors = None
        self.roof = None
    def set_attributes(self, year, make, model, doors, roof):
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
    def display_details(self):
        print("Vehicle type: {}".format(self.vehicle_type))
        print("Year: {}".format(self.year))
        print("Make: {}".format(self.make))
        print("Model: {}".format(self.model))
        print("Number of doors: {}".format(self.doors))
        print("Type of roof: {}".format(self.roof))
def main():
    car = Automobile()
    vehicle_type = "car"
    year = input("Enter the year: ")  
    make = input("Enter the make: ")  
    model = input("Enter the model: ")  
    doors = input("Enter the number of doors: ")  
    roof = input("Enter the type of roof: ")  
    car.set_vehicle_type(vehicle_type) 
    car.set_attributes(year, make, model, doors, roof) 
    print("\nCar Details:")
    car.display_details() 
if __name__ == "__main__":
    main()
# Base class
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"{self.make} {self.model}'s engine started.")

    def stop_engine(self):
        print(f"{self.make} {self.model}'s engine stopped.")

    def display_info(self):
        print(f"🚗 Vehicle Info: {self.year} {self.make} {self.model}")


# Subclass 1: Car
class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors

    def display_info(self):
        super().display_info()
        print(f" - Number of doors: {self.doors}")

    def accelerate(self):
        print(f"{self.make} {self.model} is accelerating smoothly!")


# Subclass 2: Truck
class Truck(Vehicle):
    def __init__(self, make, model, year, cargo_capacity):
        super().__init__(make, model, year)
        self.cargo_capacity = cargo_capacity  # in tons

    def display_info(self):
        super().display_info()
        print(f" - Cargo capacity: {self.cargo_capacity} tons")

    def load_cargo(self):
        print(f"{self.make} {self.model} is loading cargo...")


# Subclass 3: Motorcycle
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, drive_type):
        super().__init__(make, model, year)
        self.drive_type = drive_type  # e.g., Chain, Belt, Shaft

    def display_info(self):
        super().display_info()
        print(f" - Drive type: {self.drive_type}")

    def pop_wheelie(self):
        print(f"{self.make} {self.model} pops a wheelie!")


# Demonstration of Inheritance
def main():
    # Create objects of each subclass
    car = Car("Toyota", "Corolla", 2022, 4)
    truck = Truck("Volvo", "FH16", 2021, 18)
    bike = Motorcycle("Yamaha", "R1", 2023, "Chain")

    # Display info and call methods
    print("\n--- Car Details ---")
    car.display_info()
    car.start_engine()
    car.accelerate()
    car.stop_engine()

    print("\n--- Truck Details ---")
    truck.display_info()
    truck.start_engine()
    truck.load_cargo()
    truck.stop_engine()

    print("\n--- Motorcycle Details ---")
    bike.display_info()
    bike.start_engine()
    bike.pop_wheelie()
    bike.stop_engine()


# Run the program
if __name__ == "__main__":
    main()

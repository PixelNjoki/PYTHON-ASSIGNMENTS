# Activity 2: Polymorphism Challenge
# Vehicles with the same action move()

class Vehicle:
    def move(self):
        print("The vehicle moves in some way.")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Create objects
vehicles = [Car(), Plane(), Boat()]

# Call move() for each
for v in vehicles:
    v.move()

class Car :
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Drive")
class Boat :
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Sail")

class Plane :
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Fly")

car_1 = Car("Toyota", "Corolla")
boat_1 = Boat("Yamaha", "242X")
plane_1 = Plane("Boeing", "747")

for x in (car_1, boat_1, plane_1):
    x.move()  # Polymorphic behavior

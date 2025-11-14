class Car:
    plate_number = 12346
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0
    def __str__(self):
        return f'This is a {self.brand}, {self.model}, {self.year}'
    def accelerate(self, amount):
        self.speed += amount
        return f'This is a {self.brand}, {self.model}, {self.year} moving at {self.speed}km per hr'    
    def brake(self, amount):
        self.speed -= amount
        if self.speed >= 0 : 
            return f'This is a {self.brand}, {self.model}, {self.year} reducing speed {self.speed}km per hr'
        else:
            return f'This is a {self.brand}, {self.model}, {self.year} reducing speed 0km per hr'


car_1 = Car("Mercedes","C300", 2025)
car_2 = Car("Ford","Mustang", 2023)
# print(car_1)
# car_2.model = "Sedan"
# print(car_2.model)
print(car_1.accelerate(50))
print(car_1.brake(60))
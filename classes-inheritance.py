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

class Mercedes(Car):
    def __init__(self, model, year, color):
        super().__init__("mercedes", model, year)
        self.color = color
    def __str__(self):
        return f'This is a {self.year} {self.color} {self.model} Mercedes.'

Mercedes_1 = Mercedes( "Model S", 2024, "Black")
print(Mercedes_1)
print(Mercedes_1.accelerate(70))
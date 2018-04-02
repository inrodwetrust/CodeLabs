class Car:
    number_of_wheels = 4  # shared

    def __init__(self, color, number_of_doors, sound):
        self.color = color
        self.number_of_doors = number_of_doors
        self.horn = sound


car_1 = Car('Red', '2-Door', 'Honk!')

print(car_1.horn)

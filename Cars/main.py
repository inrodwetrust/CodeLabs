class Car:
    number_of_wheels = 4  # shared

    def __init__(self, color, number_of_doors, sound):
        self.color = color
        self.doors = number_of_doors
        self.sound = sound

    def description(self):
        return '{}, {}, {}'.format(self.color, self.doors, self.sound)


car_1 = Car('Red', '2-Door', 'Honk!')
car_2 = Car('Blue', '3-Door', 'Squeak!')
car_3 = Car('White', '4-Door', "Aaaahuuuuga!")

print(Car.description(car_1))
print(Car.description(car_2))
print(Car.description(car_3))

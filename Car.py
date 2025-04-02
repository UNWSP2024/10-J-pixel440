class Car:
    def __init__(self, year_model, make):
        self.year_model = year_model
        self.make = make
        self.speed = 0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def get_speed(self):
        return self.speed

my_car = Car(2019, "Ferari")


for _ in range(5):
    my_car.accelerate()
    print(f"Current speed (accelerating): {my_car.get_speed()} mph")


for _ in range(5):
    my_car.brake()
    print(f"Current speed (braking): {my_car.get_speed()} mph")





























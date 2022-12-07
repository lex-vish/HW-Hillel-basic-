# Створіть клас "Транспортний засіб" та підкласи "Автомобіль", "Літак", "Корабель", наслідувані від "Транспортний засіб". Наповніть класи атрибутами на свій розсуд. Створіть обʼєкти класів "Автомобіль", "Літак", "Корабель".

class Vihicle:
    speed = None
    time = None

    def __init__(self, new_speed, new_time):
        self.speed = new_speed
        self.time = new_time

    def path(self):
        res = self.speed * self.time
        return res

class Аutomobile(Vihicle):
    environment = 'land'

class Airplane(Vihicle):
    environment = 'air'

class Ship(Vihicle):
    environment = 'water'

auto1 = Аutomobile(new_speed=60, new_time=3)
plane1 = Airplane(new_speed=900, new_time=2)
ship1 = Ship(new_speed=30, new_time=2)

print(f'The car was traveling for {auto1.time} at a speed of {auto1.speed} km/h and traveled {auto1.path()} km on the {auto1.environment}.')
print(f'The plane was traveling for {plane1.time} at a speed of {plane1.speed} km/h and traveled {plane1.path()} km in the {plane1.environment}.')
print(f'The ship was traveling for {ship1.time} at a speed of {ship1.speed} km/h and traveled {ship1.path()} km on the {ship1.environment}.')

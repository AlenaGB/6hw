class Car:
    # atributes
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f'{self.name} в джижении'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'Текущая скорость {self.name} {self.speed} км/ч'

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость городского автомобиля {self.name}  {self.speed} км/ч ')

        if self.speed > 40:
            return f'Скорость {self.name} выше разрешенной'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость служебного автомобиля {self.name}  {self.speed} км/ч ')

        if self.speed > 60:
            return f'скорость {self.name} выше разрешенной'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} - полицейский автомобиль'
        else:
            return f'{self.name} - автомобиль физического лица'

honda = SportCar(98, 'красный', 'Honda', False)
kia = PoliceCar(61, 'черный', 'Kia', True)
opel = WorkCar(61, 'белый', 'Opel', False)

print(honda.turn_left())
print(f' {honda.turn_right()}, {kia.stop()}')
print(f'{kia.go()} {kia.show_speed()}')
print(f'{honda.name} {honda.color}')
print('чей это автомобиль?', kia.police())
print(opel.show_speed())
print(honda.show_speed())
print(kia.show_speed())
print(kia.police())
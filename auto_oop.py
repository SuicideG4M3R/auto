class Auto:
    def __init__(self, brand, max_speed):
        self.brand = brand
        self.speed = 0
        self.max_speed = max_speed
        self.engine = False

    def start_engine(self):
        if not self.engine:
            self.engine = True
            print('silnik odpalony')
        else:
            print('Silnik był juz odpalony')

    def stop_engine(self):
        if self.speed == 0:
            self.engine = False
            print('silnik zgaszony')
        else:
            print('pierw zatrzymaj auto')

    def speed_up(self, amount):
        if self.engine:
            self.speed = min(self.speed + amount, self.max_speed)
            print(f"Jedziesz z prędkością {self.speed}")
        else:
            print('Odpal silnik')

    def slow_down(self, amount):
        self.speed = max(self.speed - amount, 0)
        print(f"Jedziesz z prędkością {self.speed}")


bmw = Auto('bmw', 310)
fiat = Auto('fiat', 160)

# Auto.speed_up(bmw, 100)
bmw.speed_up(100)
bmw.speed_up(100)
bmw.start_engine()
fiat.speed_up(50)
bmw.speed_up(100)
bmw.speed_up(100)
bmw.speed_up(200)
bmw.stop_engine()
bmw.slow_down(150)
bmw.slow_down(150)
bmw.slow_down(150)
bmw.stop_engine()

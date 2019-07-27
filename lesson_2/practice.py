if __name__ == '__main__':
    class Auto:
        _color = 'White'
        _seats = 4
        _wheels = 4
        _engine = 3.0
        _doors = 4

        def get_seats(self):
            return self._seats

        def get_wheels(self):
            return self._wheels

        def get_engine(self):
            return self._engine

        def get_doors(self):
            return self._doors

        def get_color(self):
            return self._color

        def beep(self):
            print('BEEEP!!')

    class Car(Auto):
        _color = 'red'
        _doors = 2

        def beep(self):
            print('Beep is broken\n')

    class Truck(Auto):
        _wheels = 8
        _engine = 3.0

        def beep(self):
            print('BEEEEP-BEEEEP')

    ford = Car()
    print(f'Seats - {ford.get_seats()}')
    print(f'Color - {ford.get_color()}')
    print(f'Doors - {ford.get_doors()}')
    print(f'Engine - {ford.get_engine()}')
    ford.beep()

    truck = Truck()
    print(f'Wheels - {truck.get_wheels()}')
    print(f'Engine - {truck.get_engine()}')
    print(f'Color - {truck.get_color()}')
    truck.beep()


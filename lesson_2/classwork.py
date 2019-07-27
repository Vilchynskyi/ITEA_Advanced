if __name__ == '__main__':
    class Animal:
        animals_created = 0

        def __init__(self, name, animal_type):
            self.name = name
            self.animal_type = animal_type
            Animal.animals_created += 1

        def move(self):
            print("I am moving")

        def eat(self):
            print('I am eating')

        def sleep(self):
            print('I am eating')

        def who_am_i(self):
            print(f'I am the {self.name}. My type is {self.animal_type}')


    some_animal = Animal('Sparrow', 'Bird')
    another_animal = Animal('Spider', 'Insect')
    print(Animal.animals_created)
    some_animal.eat()
    some_animal.move()
    some_animal.sleep()
    some_animal.who_am_i()

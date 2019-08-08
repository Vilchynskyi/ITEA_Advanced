from abc import ABC, abstractmethod
from datetime import date


class Person(ABC):

    def __init__(self, name, date_of_birth):
        self._name = name
        self._date_of_birth = date_of_birth

    @abstractmethod
    def get_info(self):
        return f'{self._name} is {self.get_age()} years old'

    @abstractmethod
    def get_age(self):
        today = date.today()
        return today.year - self._date_of_birth.year - \
               ((today.month, today.day) < (self._date_of_birth.month,
                                            self._date_of_birth.day))


class Enrollee(Person):

    def __init__(self, name, year_of_birth, faculty):
        super().__init__(name, year_of_birth)
        self._faculty = faculty

    def get_info(self):
        return f'{super().get_info()}, he enrolls on {self._faculty} faculty'

    def get_age(self):
        return super().get_age()

    def get_name(self):
        return self._name


class Student(Person):

    def __init__(self, name, year_of_birth, faculty, course):
        super().__init__(name, year_of_birth)
        self._faculty = faculty
        self._course = course

    def get_info(self):
        return f'{super().get_info()}, he studies on {self._faculty} ' \
            f'on the {self._course}th course'

    def get_age(self):
        return super().get_age()

    def get_name(self):
        return self._name


class Teacher(Person):

    def __init__(self, name, year_of_birth, faculty, office, experience):
        super().__init__(name, year_of_birth)
        self._faculty = faculty
        self._office = office
        self._experience = experience

    def get_info(self):
        return f'{super().get_info()}. He is working on {self._faculty}'\
                f' as a {self._office} {self._experience} for years'

    def get_age(self):
        return super().get_age()

    def get_name(self):
        return self._name


persons = [Enrollee('Max Johnson', date(1999, 1, 26), 'IT'),
           Student('Bob Smith', date(1987, 3, 30), 'IT', 4),
           Teacher('Carl Jones', date(1969, 7, 19), 'IT', 'teacher', 12)]

age = 34

for person in persons:
    print(person.get_info())
    if person.get_age() < age:
        print(f'{person.get_name()} fits the search.')

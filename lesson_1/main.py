if __name__ == '__main__':
    numbers = list()
    for i in range(1, 100):
        if i % 2 == 0:
            numbers.append(i)
    print(numbers)

    world = {'USA': 'Washington DC',
             'Ukraine': 'Kyiv',
             'Poland': 'Warsaw',
             'German': 'Berlin',
             'Spain': 'Madrid'}
    countries = ['USA', 'Italy', 'Spain', 'Ukraine']
    for c in countries:
        if c in world:
            print(world.get(c))

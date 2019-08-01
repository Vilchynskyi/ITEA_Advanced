if __name__ == '__main__':
    func = lambda x, y: x + y
    print(func(1, 3))

    list_var = [-4, 34, 454, -12123, 354, 0]

    map_var = list(map(lambda x: x ** 2, list_var))
    print(map_var)

    map_var = list(filter(lambda x: x > 0, list_var))
    print(map_var)

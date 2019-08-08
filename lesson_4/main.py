if __name__ == '__main__':
    my_var = list()


    class A:
        pass


    print(type(my_var))
    B = type('MyNewClass', (), {'var_in_class': 'yes'})

    print(A)
    print(B)

    b = B()

    print(b.__dict__)

    print(B.__dict__)

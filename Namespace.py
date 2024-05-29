a = 6


def test_function(x):
    a = x ** 2


    def inner_function():
        global a
        print("Я в области видимости функции test_function")

        if a >= 10:
            print(f'{a} больше 10')
        else:
            print(f'{a} меньше 10')

    inner_function()
    return a


print(test_function(5))
# inner_function() - NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
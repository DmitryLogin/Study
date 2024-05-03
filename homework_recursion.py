def test(*params):
    print("Тип:", type(params))
    print(f"Аргументы: {params}")
    for i in params:
        print(i)

test('привет', 11, [11, 54])


n = int(input("Введите число: "))

def factorial(n):
    if (n <= 1):
        return 1
    else:
        return (n * factorial(n-1))


print(factorial(n))




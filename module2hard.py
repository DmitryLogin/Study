
number_1 = int(input('Введите число от 3 до 20: '))


list_number = []
for i in range(number_1):
    number_2 = (i + 1)
    for a in range(number_1):
        number_3 = (a + 1)
        sum_number = number_2 + number_3
        if sum_number == number_1:
            list_number.append(number_2)
            list_number.append(number_3)


print(list_number)
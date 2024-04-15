x = 38
print('Доброго времени суток')

if x < 0:
    print('меньше нуля')

print('Досвидания')

a, b = 10, 5

if a > b:
    print('a > b')

if a > b and a > 0:
    print('успех')

if (a > b) and (a > 0 or b < 1000):
    print('успех1')

if 5 < b and b < 10:
    print('успех2')

if '34' > '123':
    print('успех3')

if '123' > '12':
    print('успех4')

if [1, 2] > [1, 1]:
    print('успех5')

# if 6 > '5':
#     print('успех6')
#
# if 6 > [5, 6]:
#     print('успех7')

if '6' != 5:
    print('успех8')

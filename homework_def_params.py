def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)



print_params()
print_params(a = 'Привет', b = 25, c = [1,2,3])
print_params(b = 25)                #работает
print_params(c = [1,2,3])           #работает


values_list = [1, 'строка', True]
values_dict = {'a' : 'Привет', 'b' : 25, 'c' : [1,2,3]}

print_params(*values_list)
print_params(**values_dict)


values_list_2 = [1, 'строка']

print_params(*values_list_2, 42)    #работает
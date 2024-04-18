immutable_var = 1, 2, 'ctring', True, 5.7
print(immutable_var)

# immutable_var[2] = 48
# TypeError: 'tuple' object does not support item assignment - объекты tuple не поддерживают их изменение.

immutable_var = 1, 2, 'ctring', True, 5.7
print(immutable_var)

mutable_list = [1, 2, 'ctring', True, 5.7]
mutable_list[-1] = 48
print(mutable_list)

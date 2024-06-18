
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(data_structure):
    otvet = 0
    for i in data_structure:
        i_type = type(i)
        if i_type == str:
            otvet += len(i)
        elif i_type == int:
            otvet += i
        elif i_type in [list,tuple,set]:
            otvet += (calculate_structure_sum(i))
        elif i_type == dict:
            otvet += calculate_structure_sum(i.keys())
            otvet += calculate_structure_sum(i.values())
    return otvet


result = calculate_structure_sum(data_structure)
print(result)

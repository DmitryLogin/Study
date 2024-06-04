data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

list_1 = []


def calculate_structure_sum(*args):
    for i in args:
        if isinstance(i, str):
            list_1.append(len(i))
        elif isinstance(i, int):
            list_1.append(i)
        elif isinstance(i, list):
            for j in i:
                calculate_structure_sum(j)
        elif isinstance(i, dict):
            for j in i:
                calculate_structure_sum(j)
        else:
            for j in i:
                calculate_structure_sum(j)
    return sum(list_1)


result = calculate_structure_sum(data_structure)
print(result)

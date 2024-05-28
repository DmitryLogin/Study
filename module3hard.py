
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def fun_1(*args):
    for i in args:
        if isinstance(i, str):
            print(len(i))
        if isinstance(i, int):
            print(i)
        if isinstance(i, list):
            for j in i:
                if isinstance(j, str):
                    print(len(i))
                if isinstance(j, int):
                    print(j)
        if isinstance(i, dict):
            for j in i:
                if isinstance(j, str):
                    print(len(i))
                if isinstance(j, int):
                    print(j)
        if isinstance(i, tuple):
            for j in i:
                if isinstance(j, str):
                    print(len(i))
                if isinstance(j, int):
                    print(j)
def calculate_structure_sum(args):
    for j in args:
        if isinstance(j, str):
            fun_1(j)
        if isinstance(j, int):
            fun_1(j)
        if isinstance(j, list):
            fun_1(j)
        if isinstance(j, dict):
            fun_1(j)
        if isinstance(j, tuple):
            fun_1(j)





result =calculate_structure_sum(data_structure)

print(result)



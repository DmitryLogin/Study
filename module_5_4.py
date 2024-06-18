class Buiding():
    code = 1
    id = 0

    def __init__(self):
        self.id = Buiding.code
        Buiding.code += 1


for i in range(40):
    i = Buiding()
    print(i.id)







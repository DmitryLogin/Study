
class House():
    def __init__(self, name):
        self.name = name
        self.numberOfFloors = 0


    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(f'Теперь вы на этаже {self.numberOfFloors} в нашем комплексе {self.name} ')




h1 = House('Арт плаза')
h1.setNewNumberOfFloors(23)
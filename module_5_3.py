
class Building():
    def __init__(self, floor, buildingType):
        self.numberOfFloors = floor
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType

    def __lt__(self, other):
        return self.numberOfFloors < other.numberOfFloors

    def __gt__(self, other):
        return self.numberOfFloors > other.numberOfFloors

    def __ne__(self, other):
        return self.numberOfFloors != other.numberOfFloors


h1 = Building(23, 'ЖК Горский')
h2 = Building(52, 'ЖК Горский')
print(h1 == h2)
print(h1 < h2)
print(h1 != h2)

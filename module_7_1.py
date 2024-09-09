from pprint import pprint


class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = str(weight)
        self.category = str(category)

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop(Product):
    def get_products(self):
        __file_name = 'products.txt'
        file = open(__file_name, 'r')
        pprint(file.read())
        file.close()

    def add(self, *products):

        file = open('products.txt', 'r+')
        f = file.read()
        if str(products) in f:
            print(f'Продукт {products} уже есть в магазине')
        else:
            file.write(f'\n{products}')
        file.close()


s1 = Shop(1, 1, 1)
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())


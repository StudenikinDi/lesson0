from pprint import pprint


class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        str_ = str(f'{self.name}, {self.weight}, {self.category}')
        return str_


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        file_ = file.read()
        file.close()
        return file_

    def add(self, *products):
        have_product = self.get_products()
        for i in products:
            if i.name not in have_product:
                file = open(self.__file_name, 'a')
                file.write(i.__str__() + '\n')
                file.close()
            elif i.name in have_product:
                print(f'Продукт {i.name} уже есть в магазине')

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
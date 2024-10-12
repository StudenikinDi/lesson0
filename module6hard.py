
class Figure:
    sides_count = 0
    def __init__(self, color , sides ):
        self.__sides = list(sides)
        self.__color = list(color)
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 < r <= 255 and 0 < g <= 255 and 0 < b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *args):
        if len(args) != self.sides_count:
            return False
        for i in range(len(args)):
            if not isinstance(args[i], int):
                return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        perimeter = 0
        for length in self.__sides:
            perimeter += length
        return perimeter

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1
    
    def __init__(self,__color, *sides):
        if len(sides) == self.sides_count:
            super().__init__(__color, sides)
            self.__radius = super().__len__() / (2 * 3.14)
        else:
            super().__init__(__color, [1] * self.sides_count)
            self.__radius = 1 / (2 * 3.14)

    def get_square(self):
        square = 3.14 * (self.__radius ** 2)
        return square


class Triangle(Figure):
    sides_count = 3

    def __init__(self,__color, *sides):
        if len(sides) == self.sides_count:
            super().__init__(__color, sides)
        else:
            super().__init__(__color, [1] * self.sides_count)

    def get_square(self):
        half_p = super().__len__() / 2
        s1, s2, s3 = self.get_sides()
        square = (half_p * (half_p - s1) * (half_p - s2) * (half_p - s3)) ** 0.5
        return square

class Cube(Figure):
    sides_count = 12

    def __init__(self,__color, *sides):
        if len(sides) == self.sides_count:
            super().__init__(__color, list(sides))
        elif len(sides) == 1:
            super().__init__(__color, [sides[0]] * self.sides_count)
        else:
            super().__init__(__color, [1] * self.sides_count)

    def get_volume(self):
        h = self.get_sides()
        volume = h[0] ** 3
        return volume


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
import math


class Shape:
    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError

    def vertices(self):
        raise NotImplementedError


class Triangle(Shape):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.x3, self.y3 = x3, y3

    def area(self):
        return abs((self.x1 * (self.y2 - self.y3) + self.x2 * (self.y3 - self.y1) + self.x3 * (self.y1 - self.y2)) / 2)

    def perimeter(self):
        return (math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) +
                math.sqrt((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2) +
                math.sqrt((self.x1 - self.x3) ** 2 + (self.y1 - self.y3) ** 2))

    def vertices(self):
        return 3


class Rectangle(Shape):
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2

    def area(self):
        return abs((self.x2 - self.x1) * (self.y2 - self.y1))

    def perimeter(self):
        return 2 * (abs(self.x2 - self.x1) + abs(self.y2 - self.y1))

    def vertices(self):
        return 4


class Circle(Shape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

    def vertices(self):
        return 0  # У круга нет углов


def main():
    shapes = []

    while True:
        user_input = input("Введите фигуру или 'exit' для выхода: ")
        if user_input.lower() == 'exit':
            break

        parts = user_input.split()
        shape_type = parts[0]

        try:
            if shape_type == 'triangle':
                shapes.append(
                    Triangle(float(parts[1]), float(parts[2]), float(parts[3]), float(parts[4]), float(parts[5]),
                             float(parts[6])))
            elif shape_type == 'rectangle':
                shapes.append(Rectangle(float(parts[1]), float(parts[2]), float(parts[3]), float(parts[4])))
            elif shape_type == 'circle':
                shapes.append(Circle(float(parts[1]), float(parts[2]), float(parts[3])))
            else:
                print("Неизвестный тип фигуры.")
                continue
        except (ValueError, IndexError):
            print("Ошибка ввода. Проверьте параметры фигуры.")
            continue

    while True:
        command = input("Введите команду (area, perimeter, vertices) или 'exit' для выхода: ")
        if command.lower() == 'exit':
            break

        if command == 'area':
            total_area = sum(shape.area() for shape in shapes)
            print(f"Общая площадь: {total_area:.2f}")
        elif command == 'perimeter':
            total_perimeter = sum(shape.perimeter() for shape in shapes)
            print(f"Суммарный периметр: {total_perimeter:.2f}")
        elif command == 'vertices':
            total_vertices = sum(shape.vertices() for shape in shapes)
            print(f"Суммарное количество углов: {total_vertices}")
        else:
            print("Неизвестная команда.")


if __name__ == "__main__":
    pass # Ваш код здесь

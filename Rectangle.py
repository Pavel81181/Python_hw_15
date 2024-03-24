import logging
import argparse

logging.basicConfig(filename='Log.log',
                    filemode='a',
                    encoding='utf-8',
                    format='{asctime} {levelname:<8} функция "{funcName}()" строка {lineno:>3d} : {msg}',
                    style='{',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


class Rectangle:
    def __init__(self, width, length=None):
        self.width = width
        if width < 0:
            logger.error('Ширина не может быть меньше нуля')
            raise ValueError
        if length:
            self.length = length
        else:
            self.length = width

    def perimeter(self):
        logger.info(f' Периметр прямоугольника:  {self.width} и {self.length} = {2 * self.width + 2 * self.length}  ')
        return 2 * self.width + 2 * self.length

    def area(self):
        logger.info(f' Площадь прямоугольника:  {self.width} и {self.length} = {self.width * self.length}  ')
        return self.length * self.width

    def __add__(self, other):
        perimeter = self.perimeter() + other.perimeter()
        length = self.length + other.length
        width = perimeter / 2 - length
        logger.info(f' Результат сложения прямоугольников {self} и {other} :  {Rectangle(width, length)}  ')
        return Rectangle(width, length)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        perimeter = self.perimeter() - other.perimeter()
        length = abs(self.length - other.length)
        width = abs(perimeter / 2 - length)
        logger.info(f' Результат вычитания прямоугольников:  {Rectangle(width, length)}')
        return Rectangle(width, length)


    def __str__(self):
        return f' Длина прямоугольника = {self.length}, ширина прямоугольника = {self.width}'

def parse():
    parser = argparse.ArgumentParser(
        description='Получаем размеры прямоугольника',
        epilog='При отсутствии значения длины, считаем что прямоугольник - это квадрат',
        prog='Rectangle()')
    parser.add_argument('-w', '--width',  help='Введите ширину: ')
    parser.add_argument('-l', '--length', default=None, help='Введите длину: ')
    args = parser.parse_args()
    return Rectangle(int(args.width), int(args.length))

if __name__ == '__main__':
    rectangle_1 = parse()
    rectangle_2 = Rectangle(4, 2)
    print(rectangle_1.perimeter())
    print(rectangle_2.perimeter())
    print(rectangle_1.area())
    print(rectangle_2.area())
    print(rectangle_1 + rectangle_2)
    print(rectangle_1 - rectangle_2)


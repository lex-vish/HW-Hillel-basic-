# Доопрацюйте всі реревірки на типи даних (x, y в Point, begin, end в Line, etc) - зробіть перевірки за допомогою property або класса-дескриптора.
# Доопрацюйте класс Triangle з попередньої домашки наступним чином:
# обʼєкти классу Triangle можна порівнювати між собою (==, !=, >, >=, <, <=) за площею.
# перетворення обʼєкту классу Triangle на стрінг показує координати його вершин у форматі x1, y1 -- x2, y2 -- x3, y3

class Point:
    x = None
    y = None

    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be int")

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be int")


class Line(Point):
    begin = None
    end = None

    def __init__(self, begin, end):
        self._begin = begin
        self._end = end

    @property
    def begin(self):
        return self._begin

    @begin.setter
    def begin(self, Point):
        if not isinstance(begin, Point):
            raise TypeError("begin must be Point")

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, end):
        if not isinstance(end, Point):
            raise TypeError("end must be class Point ")

    def length(self):
        res = ((self.begin.x - self.end.x)**2 + (self.begin.y - self.end.y)**2)**0.5
        return res


class Triangle(Line):
    first_point = None
    second_point = None
    third_point = None

    def __init__(self, first_point, second_point, third_point):
        self._first_point = first_point
        self._second_point = second_point
        self._third_point = third_point

    @property
    def first_point(self):
        return self._first_point

    @first_point.setter
    def first_point(self, Point):
        if not isinstance(first_point, Point):
            raise TypeError

    @property
    def second_point(self):
        return self._second_point

    @second_point.setter
    def second_point(self, Point):
        if not isinstance(second_point, Point):
            raise TypeError

    @property
    def third_point(self):
        return self._third_point

    @third_point.setter
    def third_point(self, Point):
        if not isinstance(third_point, Point):
            raise TypeError

    def area(self):
        side12 = Line(self.first_point, self.second_point).length()
        side13 = Line(self.first_point, self.third_point).length()
        side23 = Line(self.second_point, self.third_point).length()
        sp = 0.5 * (side12 + side13 + side23)
        res = (sp*(sp - side12)*(sp - side13)*(sp - side23)) ** 0.5
        return res

    def __eq__(self, other):  # ==
        return self.area() == other.area()


    def __ne__(self, other):  # !=
        return self.area() != other.area()

    def __gt__(self, other):  # >
        return self.area() > other.area()

    def __ge__(self, other):  # >=
        return self.area() >= other.area()

    def __lt__(self, other):  # <
        return self.area() < other.area()

    def __le__(self, other):  # <=
        return self.area() <= other.area()

    def to_str(self):
        return f'{str(self.first_point.x)},{str(self.first_point.y)}--{str(self.second_point.x)},{str(self.second_point.y)}--{str(self.third_point.x)},{str(self.third_point.y)}'


point1 = Point(0, 0)
point2 = Point(0, 5)
point3 = Point(4, 0)
point4 = Point(2, 10)

first_triangle = Triangle(point1, point2, point3)
second_triangle = Triangle(point1, point2, point4)
third_triangle = Triangle(point3, point2, point1)

print(first_triangle.area())
print(second_triangle.area())
print(third_triangle.area())
print(first_triangle.to_str())
print(second_triangle.to_str())
print(first_triangle == second_triangle, second_triangle != first_triangle)
print(first_triangle > second_triangle, first_triangle < second_triangle)
print(first_triangle >= second_triangle, first_triangle <= second_triangle)
print(second_triangle > second_triangle, first_triangle <= second_triangle)
print(first_triangle == third_triangle)
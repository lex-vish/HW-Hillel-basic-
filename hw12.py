# Доопрацюйте класс Point так, щоб в атрибути x та y обʼєктів цього класу можна було записати тільки обʼєкти класу int або float
# Доопрацюйте класс Line так, щоб в атрибути begin та end обʼєктів цього класу можна було записати тільки обʼєкти класу Point
# Створіть класс Triangle (трикутник), який задається трьома точками (обʼєкти классу Point). Реалізуйте перевірку даних, аналогічно до класу Line. Визначет метод, що містить площу трикутника. Для обчислень можна використати формулу Герона (https://en.wikipedia.org/wiki/Heron%27s_formula)

class Point:
    x = None
    y = None

    def __init__(self, x, y):
        # check here numbers
        if not isinstance(x, (int, float)):
            raise TypeError
        if not isinstance(y, (int, float)):
            raise TypeError
        self.x = x
        self.y = y


class Line(Point):
    begin = None
    end = None

    def __init__(self, begin, end):
        # check here Point
        if not isinstance(begin, Point):
            raise TypeError
        if not isinstance(end, Point):
            raise TypeError
        self.begin = begin
        self.end = end

    def length(self):
        res = ((self.begin.x - self.end.x)**2 + (self.begin.y - self.end.y)**2)**0.5
        return res


class Triangle(Line):
    first_point = None
    second_point = None
    third_point = None

    def __init__(self, first_point, second_point, third_point):
        # check here Point
        if not isinstance(first_point, Point):
            raise TypeError
        if not isinstance(second_point, Point):
            raise TypeError
        if not isinstance(third_point, Point):
            raise TypeError
        self.first_point = first_point
        self.second_point = second_point
        self.third_point = third_point

    def area(self):
        side12 = Line(self.first_point, self.second_point).length()
        side13 = Line(self.first_point, self.third_point).length()
        side23 = Line(self.second_point, self.third_point).length()
        sp = 0.5 * (side12 + side13 + side23)
        res = (sp*(sp - side12)*(sp - side13)*(sp - side23)) ** 0.5
        return res


point1 = Point(0, 0)
point2 = Point(0, 3)
point3 = Point(4, 0)

my_triangle = Triangle(point1, point2, point3)
print(my_triangle.area())
class RedCircle:
    pass


class BlueRecttangle:
    pass


"""
在還沒有bridge 之前的物件
"""


class Color:
    def render_color(self):
        pass


class Shape:
    def __init__(self, color):
        self.color = color()

    def draw(self):
        pass


class Red(Color):
    pass


class Circle(Shape):
    pass


red_circle = Circle(Red)
red_circle.draw()

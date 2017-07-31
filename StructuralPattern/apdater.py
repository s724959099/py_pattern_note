class Shape:
    def draw(self):
        pass


class Rectangle(Shape):
    def draw(self):
        print("draw rectangle")


class Circle:
    def draw_circle(self):
        print("draw circle")


class Drawer:
    def draw(self, shape):
        shape.draw()


class AdapterCircle:
    def __init__(self):
        self.circle = Circle()

    def draw(self):
        return self.circle.draw_circle()


circle = AdapterCircle()
drawer = Drawer()
drawer.draw(circle)

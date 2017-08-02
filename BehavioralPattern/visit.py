class Wheel:
    def __init__(self, name):
        self.name = name

    def accept(self, visitor):
        # 每個visitor是同樣的，但是其中的方法是不一樣的，比如這裡是visitWheel，
        # 然後傳入瞭self，想想？他其實想做什麼就能做什麼
        visitor.visit_wheel(self)


class Engine:
    def accept(self, visitor):
        visitor.visit_engine(self)


class Body:
    def accept(self, visitor):
        visitor.visit_body(self)


# 我們要組合成車
class Car:
    def __init__(self):
        self.engine = Engine()
        self.body = Body()
        self.wheels = [Wheel("front left"), Wheel("front right"),
                       Wheel("back left"), Wheel("back right")]

    # 這個也不需要在動，他隻是上面部件的組合，隻是做瞭屬性的委托
    def accept(self, visitor):
        visitor.visit_car(self)
        self.engine.accept(visitor)
        self.body.accept(visitor)
        for wheel in self.wheels:
            wheel.accept(visitor)


# 這個才是我們的訪問者，每次的修改都在這裡面
class PrintVisitor:
    def visit_wheel(self, wheel):
        print("Visiting " + wheel.name + " wheel")

    def visit_engine(self, engine):
        print("Visiting engine")

    def visit_body(self, body):
        print("Visiting body")

    def visit_car(self, car):
        print("Visiting car")


if __name__ == '__main__':
    car = Car()
    visitor = PrintVisitor()
    car.accept(visitor)

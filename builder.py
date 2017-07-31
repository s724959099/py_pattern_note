class Decorator:
    def __init__(self, builder):
        self.builder = builder()
        self.builder.fn1()
        self.builder.fn2()
        self.builder.fn3()
        self.builder.fn4()


class Builder:
    def fn1(self):
        pass

    def fn2(self):
        pass

    def fn3(self):
        pass

    def fn4(self):
        pass


decorator = Decorator(Builder)
builder = decorator.builder

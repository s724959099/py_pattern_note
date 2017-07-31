class FlyweightMixin:
    _instances = {}

    def __init__(self):
        raise NotImplementedException

    def __new__(cls, *args, **kwargs):
        return cls._instances.setdefault(
            # 需要cls作为键值的一部分
            (cls, args, tuple(kwargs.items())),
            # 通过super和type调用享元类进行实例化
            super(type(cls), cls).__new__(cls, *args, **kwargs))


class Spam(FlyweightMixin):
    def __init__(self, a, b):
        self.a = a
        self.b = b


class Egg(FlyweightMixin):
    def __init__(self, x, y):
        self.x = x
        self.y = y


spam1 = Spam(1, 2)
spam2 = Spam(1, 2)

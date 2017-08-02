class Singleton:
    __singleton = None

    @classmethod
    def get_instance(cls):
        if not isinstance(cls.__singleton, cls):
            cls.__singleton = cls()
        return cls.__singleton


class Test(Singleton):
    def test(self):
        print(self.__class__, id(self))


t = Test.get_instance()
t.test()
t2 = Test.get_instance()
t2.test()

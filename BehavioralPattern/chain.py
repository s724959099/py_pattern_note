class Chain:
    instance = {}

    def __init__(self, name="__global__"):
        self.name = name
        if name not in self.instance:
            self.instance[self.name] = []

    def __call__(self, fn):
        print("Call")
        self.instance[self.name].append(fn)

        def wrapper(*args, **kwargs):
            return fn(*args, **kwargs)

        return wrapper

    @classmethod
    def call(cls, *args, **kwargs):
        # call group name
        name = kwargs.setdefault("call_name", "__global__")
        # to next chain return data
        false_type = kwargs.setdefault("false_type", "__next__")
        del kwargs["call_name"]
        del kwargs["false_type"]
        for fn in cls.instance[name]:
            result = fn(*args, **kwargs)
            if result is not false_type and result is not None:
                break

        return result if result is not false_type else None


@Chain()
def func(r):
    if 10 < r < 20:
        print("func")
        return True
    else:
        return "__next__"


@Chain()
def func1(r):
    if 20 < r < 30:
        print("func1")
        return True
    else:
        return "__next__"


@Chain()
def fun2(r):
    if 30 < r < 40:
        print("func")
        return True
    else:
        return "__next__"


if __name__ == '__main__':
    Chain.call(args=(15,))

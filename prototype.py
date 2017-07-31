import copy


class Test:
    value = 3

    def copy(self):
        return copy.deepcopy(self)


t = Test()
t1 = t.copy()
t.value = 4
t2 = t.copy()
t.value=5

print(t2.value)

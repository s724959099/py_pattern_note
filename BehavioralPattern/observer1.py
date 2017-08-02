class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)


class HouseSale(Subject):
    def __init__(self):
        super().__init__()
        self._house = []

    def get_house(self, house):
        self._house.append(house)
        self.notify()


class Buyer:
    def update(self,subject):
        print("get update")


if __name__ == "__main__":
    h = HouseSale()
    buyer1 = Buyer()
    buyer2 = Buyer()
    buyer3 = Buyer()

    h.attach(buyer1)
    h.attach(buyer2)
    h.attach(buyer3)

    h.get_house("house 1")

class Dog:
    pass


class Cat:
    pass


class SimpleFactory:
    def get_pet(self, name):
        if name == "cat":
            return Cat()
        if name == "dog":
            return Dog()


factory = SimpleFactory()
dog = factory.get_pet("dog")
cat = factory.get_pet("cat")

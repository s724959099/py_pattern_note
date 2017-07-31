class Dog:
    pass


class DogFactory:
    def get_dog(self):
        # pre-processing
        return Dog()


dog = DogFactory()

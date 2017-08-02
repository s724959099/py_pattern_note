class Pizza:
    def season(self, season):
        pass


class PizzaFactory:
    def get_food(self, season):
        food = Pizza()
        food.season(season)
        return food


class Rice:
    def season(self, season):
        pass


class RiceFactory:
    def get_food(self, season):
        food = Rice()
        food.season(season)
        return food


class FoodStore:
    def __init__(self):
        self.factory = None

    def get_food(self, factory, season_name):
        self.factory = factory()
        return self.season(season_name)

    def season(self, season_name):
        print("我做了調味", season_name)
        return self.factory.get_food(season_name)


store = FoodStore()
pizza = store.get_food(PizzaFactory, "加辣")
rice = store.get_food(RiceFactory,"加醬油")

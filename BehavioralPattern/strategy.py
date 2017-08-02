import types


class StrategyExample:
    def __init__(self, func=None):
        self.name = 'Strategy Example 0'
        if func is not None:
            self.execute = types.MethodType(func, self)

    def execute(self):
        print(self.name)


def execute_replacement1(self):
    print(self.name + ' from execute 1')


def execute_replacement2(self):
    print(self.name + ' from execute 2')


def main1():
    s0 = StrategyExample()

    s1 = StrategyExample(execute_replacement1)
    s1.name = 'Strategy Example 1'

    s2 = StrategyExample(execute_replacement2)
    s2.name = 'Strategy Example 2'

    s0.execute()
    s1.execute()
    s2.execute()


# ----------------------------------------------------

class Player:
    attack_type = {
        "fist": 0,
        "magic": 1,
        "gun": 2,
        "sword": 3,
    }

    def __init__(self):
        self.__attack = {
            self.attack_type["fist"]: self.__fist_attck,
            self.attack_type["magic"]: self.__magic_attck,
            self.attack_type["gun"]: self.__gun_attck,
            self.attack_type["sword"]: self.__sword_attck,
        }

    def __fist_attck(self):
        print("拳頭攻擊")

    def __magic_attck(self):
        print("魔法攻擊")

    def __gun_attck(self):
        print("手槍攻擊")

    def __sword_attck(self):
        print("劍攻擊")

    def attack(self, attack_type=None):
        if attack_type is None:
            attack_type = self.attack_type["fist"]

        self.__attack[attack_type]()


def main2():
    player = Player()
    player.attack()
    player.attack(player.attack_type["magic"])
    player.attack(player.attack_type["gun"])
    player.attack(player.attack_type["sword"])
    player.attack(player.attack_type["fist"])


if __name__ == '__main__':
    # main1()
    main2()

### OUTPUT ###
# Strategy Example 0
# Strategy Example 1 from execute 1
# Strategy Example 2 from execute 2

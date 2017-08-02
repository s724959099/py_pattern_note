class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def grow_up(self, age):
        self.age = age

    def create_memento(self):
        return Memento(self.name, self.age)

    def set_memento(self, memento):
        if memento is None:
            print("no life record")
        self.name = memento.name
        self.age = memento.age

    def introduce(self):
        print("我叫{} 今年{}歲".format(self.name, self.age))


class Memento:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class CareTaker:
    def __init__(self):
        self.records = []

    def record(self, memento, record_name):
        self.records.append({
            "memento": memento,
            "name": record_name
        })

    def read(self, record_name):
        for record in self.records:
            if record["name"] is record_name:
                return record["memento"]


def main():
    person = Person("Max", 18)
    care_taker = CareTaker()
    care_taker.record(person.create_memento(), "剛進入大學")
    person.introduce()
    person.grow_up(22)
    person.introduce()
    care_taker.record(person.create_memento(), "畢業囉")
    person.grow_up(27)
    person.introduce()
    care_taker.record(person.create_memento(), "好想回到過去")
    person.set_memento(care_taker.read("剛進入大學"))
    person.introduce()


if __name__ == "__main__":
    main()

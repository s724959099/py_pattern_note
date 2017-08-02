class State:
    def __init__(self, traffic):
        self.traffic = traffic

    def toggle(self):
        raise NotImplemented


class GreenLight(State):
    def toggle(self):
        print("綠燈行")
        self.traffic.state = self.traffic.yellow


class RedLight(State):
    def toggle(self):
        print("紅燈停")
        self.traffic.state = self.traffic.green


class YellowLight(State):
    def toggle(self):
        print("黃燈小心！")
        self.traffic.state = self.traffic.red


class TrafficLight:
    def __init__(self):
        self.green = GreenLight(self)
        self.yellow = YellowLight(self)
        self.red = RedLight(self)

        self.state = self.red

    def toggle_light(self):
        self.state.toggle()


if __name__ == "__main__":
    traffic = TrafficLight()
    actions = [traffic.toggle_light] * 5
    [action() for action in actions]

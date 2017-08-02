class Player:
    def __init__(self, name, chat_room):
        self.name = name
        self.chat_room = chat_room

    def talk(self, msg, to_player=None):
        output = "{} 跟 {} 說話".format(self.name, to_player.name) if to_player else "{} 跟大家說話".format(self.name)
        print(output)
        self.chat_room.receive(msg, self, to_player)

    def get_message(self, player, msg):
        print("{} 跟我({})說 {}".format(player.name, self.name, msg))


class ChatRoom:
    def __init__(self):
        self.player_list = []

    def add_player(self, player):
        self.player_list.append(player)

    def receive(self, msg, send_player, get_player):
        if get_player is None:
            for player in self.player_list:
                player.get_message(send_player, msg)
        else:
            get_player.get_message(send_player, msg)


class PlayerFactory:
    def __init__(self, mediator):
        self.mediator = mediator

    def add_player(self, name):
        player = Player(name, self.mediator)
        self.mediator.add_player(player)
        return player


chat_room = ChatRoom()
factory = PlayerFactory(chat_room)

p1 = factory.add_player("p1")
p2 = factory.add_player("p2")
p3 = factory.add_player("p3")
p4 = factory.add_player("p4")

p1.talk("hello every body")
p1.talk("private msg", p2)

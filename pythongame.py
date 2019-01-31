import module


def next_room(self, room):

    self.room = room


class Runner(object):

    def __init__(self, room):
        self.room = room


class Death(object):

    def dialouge():
        print("You died my child")
        exit(1)


class FrontPorch(object):

    def dialouge():
        print("front porch dialouge 1 die 2 liv")
        answer = input("> ")

        if answer == '1':
            print("u die")
            Death.dialouge()
#return some value

class Lobby(object):

    pass


class Basement(object):

    pass

class Map(object):

    rooms = {
        'death' : Death(),
        'front_porch' : FrontPorch(),
    }

FrontPorch.dialouge()

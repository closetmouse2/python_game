#import module

#class Runner(object):

#    def __init__(self, scene_map):
#        self.scene_map = scene_map

#    def run(self):
#        Map.scenes[scene_map]

class FrontPorch(object):

    def dialouge():
        print("You awaken and find youself surrounded almost completely by trees...")
        input("")
        print("In a haze, you inspect your surroundings. It appears you're in the front lawn to some sort of decrepid mansion...")
        input("")
        print("It looks intimidating... What do you do? \n 1. Nope outta there and wander through the woods. \n 2. Enter the house, I ain't no baby. Maybe they know how I got here. \n 3. Walk around the back of the house")
        answer = input("> ")

        if answer == '1':
            print("You turn to leave the property...")
            input("")
            print("As you approach the woods, one of the trees grab you and rip you into 2 pieces...")
            Death.dialouge()
#            Runner('death')
        elif answer == '2':
            Lobby.dialouge()
#            Runner('lobby')
        elif answer == '3':
            print("You make your way around to the side of the house...")
            input("")
            print("As you do this, the entire house tips onto its side... Crushing you like an empty can of coke.")
            Death.dialouge()
#            Runner('death')
        else:
            print("I didn't understand that, and I hate what I don't understand. U die for this")
            Death.dialouge()
#            Runner('death')


class Lobby(object):

    def dialouge():
        print("You make your way onto the front porch and stare at the door... It's opened??")
        input("")
        print("You approach the door and enter the house. The inside smells like decaying flesh and you are immediatley overcome by an intense sense of dread..")
        input("")
        print("The door suddenly slams behind you and you're met with a dark, terrifying mansion..")
        input("")
        print("What do you do? \n 1. Try and escape the way you came \n 2. War cry like Goku and run into the darkest, scariest part of the house \n 3. Dump your pants because you're scared and mommy isn't around ")
        answer = input("> ")

        if answer == '1':
            print("You turn and try the door handle...")
            input("")
            print("Your hand gets stuck to the handle?!?!? You try and free your hand to no avail.")
            input("")
            print("The house turns into that thing from the spongebob movie with the stick tounge that tries to kill spongebob and patrick only this time its you and it actuall does kill you because this game is violent and i doubt they would actually allow spongebob and patrick to die on television for a number of reasons one of course being the brand value of the pair like nickelodeon would never kill them off because they would lose so much money cancelling the show and stuff also its a kids movie so they would prolly be scared but spongebob is kinda known to do stuff for the parents watching so who really knows")
#            Runner('death')
            Death.dialouge()
        elif answer == '2':
            Basement.dialouge()
#            Runner('basement')
        elif answer == '3':
            print("HAHAHA of course you did that...")
            input("")
            print("The house turns into that thing from the spongebob movie with the stick tounge that tries to kill spongebob and patrick only this time its you and it actuall does kill you because this game is violent and i doubt they would actually allow spongebob and patrick to die on television for a number of reasons one of course being the brand value of the pair like nickelodeon would never kill them off because they would lose so much money cancelling the show and stuff also its a kids movie so they would prolly be scared but spongebob is kinda known to do stuff for the parents watching so who really knows")
#            Runner('death')
            Death.dialouge()
        else:
            print("I didn't understand that, and I hate what I don't understand. U die for this")
            Death.dialouge()
#            Runner('death')


class Basement(object):

    def dialouge():
        print("You power up and run into the basement screaming like a true saiyan")
        input("")
        print("When you make it to the bottom of the basement steps, you notice that this is no basement; but some sort of kinky dungeon...")
        input("")
        print("When your eyes adjust to the new darkness, you look around and your eyes lock with a naked hermit.. What do you do? \n 1. Flirt \n 2. Continue making intense eye contact \n 3. Attack")
        answer = input("> ")

        if answer == '1':
            print("You begin to flirt with the hermit and eventually buy him a drink.")
            input("")
            print("Things seem to be going really well so you ask him to come back to your place...")
            input("")
            print("He hits you with a 'as if', flips his hair, and struts off. FeelsBad so you die out of sadness.")
            Death.dialouge()
#            Runner('death')
        elif answer == '2':
            print("You stare into his sweet baby blues intensly...")
            input("")
            print("Upon gazing at this mans immaculate beauty, you are reminded of all your short comings. Also btw he on bath salts so he rip your face off")
            Death.dialouge()
#            Runner('win')
        elif answer == '3':
            print("You scream once again and run towards the hermit...")
            input("")
            print("You grab the back of his neck and rip his spine out like a madman.. Just to show him who's boss you start using his spine like a lasso.")
            input("")
            print("Upon Spinning the spine around, you hit yourself by accident and die")
            Win.dialouge()
#            Runner('win')
        else:
            print("I didn't understand that, and I hate what I don't understand. U die for this")
            Death.dialouge()
#            Runner('death')


class Death(object):

    def dialouge():
        print("You died my child")
        exit(1)


class Win(object):

    def dialouge():
        print('You died but you actually WIN for redemption lies in death')
        exit(1)

#class Map(object):

#    scenes = {
#        'lobby' : Lobby.dialouge(),
#        'basement' : Basement.dialouge(),
#        'death' : Death.dialouge(),
#    }

FrontPorch.dialouge()

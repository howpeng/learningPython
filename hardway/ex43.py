from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subcalss it and implement enter()."
        exit(1)

class Engine(object):

    def __init__(self,scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print "\n-------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):

    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this."
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
        print "your entire crew. You are the last surviving member and your last"
        print "mission is to get hte neutron destruct bomb from the Weapon Armory,"
        print "put it in the bridge, and blow the ship up after getting into an"
        print "escape pod."
        print "\n"
        print "You're running down the central corridor to the Weapons Armory when"
        print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
        print "flowing around his hate filled body. he's blocking the door to the"
        print "Armory and about to pull a weapon to blast you."

    action = raw_input(">>> ")

    if action == "shoot!":
        print "Quick on the draw ou yank out your blaster and fire it at the Gothon."
        print "His clown costume is flowing and moving around his body, which throws"
        print "off your aim. Your laser hits his costume but misses him entirely. This"
        print "completely ruins his brand new costume his mother bought him, which"
        print "makes him fly into a rage and blast you repeatedly in the face until"
        print "you are dead. Then he eats you."
        return 'death'

    elif action == "dodge!":
        print "Like a world calss boxer you doddge, weave, slip and slide right"
        print "as the Gothon's blaster cranks a laser past your head."
        print "In the middle of your artful dodge uour foot slips and you"
        print "bang your head on the metal wall and pass out."
        print "You wake up shortly after only to die as the Gothon stomps on"
        print "your head and eats you."
        return 'death'

    elif action == "tell a joke":
        print "Lucky for you they made you learn Gothon insults in the academy."
        print "You tell the one Gothon joke you know:"
        print "Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr."
        print "The Gothon stoips......."
        print "putting him down, then jump through the Weapon Armory door."
        return 'laser_weapon_armory'

    else:
        print "DOSE NOT COMPUTE"
        return 'central_corridor'

class LaserWeaponArmory(Scene):

    def enter(self):
        print "You do........."
        print "k........."
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:

class LaserWeaponArmory(Scene):

    def enter(self):
        pass


class TheBridge(Scene):

    def enter(self):
        pass


class EscapePod(Scene):

    def enter(self):
        pass

class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
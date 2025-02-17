from creature import *


class Cat(Creature):
    def __init__(self, name, behavior: CreatureBehavior = CreatureBehavior(
        running=CreatureBehaviorData(True, 5),
        swimming=CreatureBehaviorData(False),
        flying=CreatureBehaviorData(False)
    )):
        self.name = name
        self.behavior = behavior



class Tiger(Creature):
    def __init__(self, name, behavior: CreatureBehavior = CreatureBehavior(
        running=CreatureBehaviorData(True, 20),
        swimming=CreatureBehaviorData(True, 40),
        flying=CreatureBehaviorData(False),
        energy=200
    )):
        self.name = name
        self.behavior = behavior


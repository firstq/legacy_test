from creature import *


class Dog(Creature):
    def __init__(self, name, behavior: CreatureBehavior = CreatureBehavior(
        running=CreatureBehaviorData(True, 10),
        swimming=CreatureBehaviorData(True, 30),
        flying=CreatureBehaviorData(False)
    )):
        self.name = name
        self.behavior = behavior


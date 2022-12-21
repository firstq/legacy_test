from creature import *


class Fish_Simple(Creature):
    def __init__(self, name, behavior: CreatureBehavior = CreatureBehavior(
        running=CreatureBehaviorData(False),
        swimming=CreatureBehaviorData(True, 5),
        flying=CreatureBehaviorData(False)
    )):
        self.name = name
        self.behavior = behavior


class Fish_Can_Fly(Creature):
    def __init__(self, name, behavior: CreatureBehavior = CreatureBehavior(
        running=CreatureBehaviorData(False),
        swimming=CreatureBehaviorData(True, 5),
        flying=CreatureBehaviorData(True, 20)
    )):
        self.name = name
        self.behavior = behavior


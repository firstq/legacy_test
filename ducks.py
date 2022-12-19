from creature import *


class Duck(Creature):
    def __init__(self, name, behavior: CreatureBehavior = CreatureBehavior(
        running=CreatureBehaviorData(False),
        swimming=CreatureBehaviorData(True, 10),
        flying=CreatureBehaviorData(True, 30)
    )):
        self.name = name
        self.behavior = behavior


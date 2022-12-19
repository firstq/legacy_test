from dataclasses import dataclass


@dataclass
class CreatureBehaviorData:
    is_can: bool
    energy_consumption: int = 0


class CreatureBehavior(object):
    def __init__(self, running: CreatureBehaviorData, swimming: CreatureBehaviorData, flying: CreatureBehaviorData, energy=100):
        self.running = running
        self.swimming = swimming
        self.flying = flying
        self.energy = energy


    def run(self, name):
        if self.running.is_can:
            print("My name is "+str(name)+" and i running")
            self.energy = self.energy - self.running.energy_consumption
        else:
            print("My name is "+str(name)+" and i can't run")


    def swim(self, name):
        if self.swimming.is_can:
            print("My name is "+str(name)+" and i swimming")
            self.energy = self.energy - self.swimming.energy_consumption
        else:
            print("My name is "+str(name)+" and i can't swim")


    def fly(self, name):
        if self.flying.is_can:
            print("My name is "+str(name)+" and i flying")
            self.energy = self.energy - self.flying.energy_consumption
        else:
            print("My name is "+str(name)+" and i can't fly")


    def get_energy(self):
        return self.energy


class Creature(object):
    def __init__(self, name, behavior: CreatureBehavior):
        self.name = name
        self.behavior = behavior


    def say(self):
        print(f"Hello, i'm {self.__class__.__name__} and my name is {self.name}")


    def get_energy(self) -> int:
        return self.behavior.energy


    def run(self):
        self.behavior.run(self.name)


    def swim(self):
        self.behavior.swim(self.name)


    def fly(self):
        self.behavior.fly(self.name)

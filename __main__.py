from cats import *
from dogs import Dog
from ducks import Duck
from fish import *

dog_name = "Bobik"
dog = Dog(dog_name)
dog.say()
dog_energy = dog.get_energy()
assert dog_energy == 100, "Bad start energy for Bobik"
dog.run()
dog_energy_after_run = dog.get_energy()
assert dog_energy_after_run == 90, "Bad after run energy for Bobik"
dog.swim()
dog_energy_after_swim = dog.get_energy()
assert dog_energy_after_swim == 60, "Bad after swim energy for Bobik"
dog.fly()
dog_energy_after_fly = dog.get_energy()
assert dog_energy_after_fly == 60, "Bad after fly energy for Bobik"

tiger_name = "Barsik"
tiger = Tiger(tiger_name)
tiger.say()
tiger_energy = tiger.get_energy()
assert tiger_energy == 200, "Bad start energy for Barsik"
tiger.run()
tiger_energy_after_run = tiger.get_energy()
assert tiger_energy_after_run == 180, "Bad after run energy for Barsik"
tiger.swim()
tiger_energy_after_swim = tiger.get_energy()
assert tiger_energy_after_swim == 140, "Bad after swim energy for Barsik"
tiger.fly()
tiger_energy_after_fly = tiger.get_energy()
assert tiger_energy_after_fly == 140, "Bad after fly energy for Barsik"

duck_name = "Donald"
duck = Duck(duck_name)
duck.say()
duck_energy = duck.get_energy()
assert duck_energy == 100, "Bad start energy for Donald"
duck.run()
duck_energy_after_run = duck.get_energy()
assert duck_energy_after_run == 100, "Bad after run energy for Donald"
duck.swim()
duck_energy_after_swim = duck.get_energy()
assert duck_energy_after_swim == 90, "Bad after swim energy for Donald"
duck.fly()
duck_energy_after_fly = duck.get_energy()
assert duck_energy_after_fly == 60, "Bad after fly energy for Donald"

fish_simple_name = "Nemo"
fish_simple = Fish_Simple(fish_simple_name)
fish_simple.say()
fish_simple_energy = fish_simple.get_energy()
assert fish_simple_energy == 100, "Bad start energy for Nemo"
fish_simple.run()
fish_simple_energy_after_run = fish_simple.get_energy()
assert fish_simple_energy_after_run == 100, "Bad after run energy for Nemo"
fish_simple.swim()
fish_simple_energy_after_swim = fish_simple.get_energy()
assert fish_simple_energy_after_swim == 95, "Bad after swim energy for Nemo"
fish_simple.fly()
fish_simple_energy_after_fly = fish_simple.get_energy()
assert fish_simple_energy_after_fly == 95, "Bad after fly energy for Nemo"

fish_can_fly_name = "Flufy"
fish_can_fly = Fish_Can_Fly(fish_can_fly_name)
fish_can_fly.say()
fish_can_fly_energy = fish_can_fly.get_energy()
assert fish_can_fly_energy == 100, "Bad start energy for Flufy"
fish_can_fly.run()
fish_can_fly_energy_after_run = fish_can_fly.get_energy()
assert fish_can_fly_energy_after_run == 100, "Bad after run energy for Flufy"
fish_can_fly.swim()
fish_can_fly_energy_after_swim = fish_can_fly.get_energy()
assert fish_can_fly_energy_after_swim == 95, "Bad after swim energy for Flufy"
fish_can_fly.fly()
fish_can_fly_energy_after_fly = fish_can_fly.get_energy()
assert fish_can_fly_energy_after_fly == 75, "Bad after fly energy for Flufy"
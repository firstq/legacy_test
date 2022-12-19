from creature import *
from cats import *
from dogs import Dog
from ducks import Duck
from fish import *

def checking(capfd, creature: Creature, expected):

    creature.say()

    out, err = capfd.readouterr()
    assert creature.get_energy() == expected['say_energy']
    assert out.replace("\n", "") == expected['say_out']

    creature.run()

    out, err = capfd.readouterr()
    assert creature.get_energy() == expected['run_energy']
    assert out.replace("\n", "") == expected['run_out']

    creature.swim()

    out, err = capfd.readouterr()
    assert creature.get_energy() == expected['swim_energy']
    assert out.replace("\n", "") == expected['swim_out']

    creature.fly()

    out, err = capfd.readouterr()
    assert creature.get_energy() == expected['fly_energy']
    assert out.replace("\n", "") == expected['fly_out']

def test_super_creature(capfd):
    name = 'Sharik'
    creature = Creature(name, CreatureBehavior(
        running=CreatureBehaviorData(True, 10),
        swimming=CreatureBehaviorData(True, 20),
        flying=CreatureBehaviorData(True, 30),
        energy=100
    ))

    expected = {
        'say_out': f"Hello, i'm Creature and my name is {name}",
        'say_energy': 100,
        'swim_out': f"My name is {name} and i swimming",
        'swim_energy': 70,
        'run_out': f"My name is {name} and i running",
        'run_energy': 90,
        'fly_out': f"My name is {name} and i flying",
        'fly_energy': 40,
    }

    checking(capfd, creature, expected)


def test_useless_creature(capfd):
    name = 'Sharik'
    creature = Creature('Sharik', CreatureBehavior(
        running=CreatureBehaviorData(False),
        swimming=CreatureBehaviorData(False),
        flying=CreatureBehaviorData(False),
        energy=100
    ))

    expected = {
        'say_out': f"Hello, i'm Creature and my name is {name}",
        'say_energy': 100,
        'swim_out': f"My name is {name} and i can't swim",
        'swim_energy': 100,
        'run_out': f"My name is {name} and i can't run",
        'run_energy': 100,
        'fly_out': f"My name is {name} and i can't fly",
        'fly_energy': 100,
    }

    checking(capfd, creature, expected)

def test_dog(capfd):
    name = 'Bobik'
    dog = Dog(name)

    expected = {
        'say_out': f"Hello, i'm Dog and my name is {name}",
        'say_energy': 100,
        'swim_out': f"My name is {name} and i swimming",
        'swim_energy': 60,
        'run_out': f"My name is {name} and i running",
        'run_energy': 90,
        'fly_out': f"My name is {name} and i can't fly",
        'fly_energy': 60,
    }

    checking(capfd, dog, expected)

def test_cat(capfd):
    name = 'Barsik'
    cat = Cat(name)

    expected = {
        'say_out': f"Hello, i'm Cat and my name is {name}",
        'say_energy': 100,
        'swim_out': f"My name is {name} and i can't swim",
        'swim_energy': 95,
        'run_out': f"My name is {name} and i running",
        'run_energy': 95,
        'fly_out': f"My name is {name} and i can't fly",
        'fly_energy': 95,
    }

    checking(capfd, cat, expected)

def test_tiger(capfd):
    name = 'Sherchan'
    tiger = Tiger(name)

    expected = {
        'say_out': f"Hello, i'm Tiger and my name is {name}",
        'say_energy': 200,
        'swim_out': f"My name is {name} and i swimming",
        'swim_energy': 140,
        'run_out': f"My name is {name} and i running",
        'run_energy': 180,
        'fly_out': f"My name is {name} and i can't fly",
        'fly_energy': 140,
    }

    checking(capfd, tiger, expected)

def test_duck(capfd):
    name = 'Donald'
    duck = Duck(name)

    expected = {
        'say_out': f"Hello, i'm Duck and my name is {name}",
        'say_energy': 100,
        'swim_out': f"My name is {name} and i swimming",
        'swim_energy': 90,
        'run_out': f"My name is {name} and i can't run",
        'run_energy': 100,
        'fly_out': f"My name is {name} and i flying",
        'fly_energy': 60,
    }

    checking(capfd, duck, expected)

def test_fish(capfd):
    name = 'Nemo'
    fish = Fish_Simple(name)

    expected = {
        'say_out': f"Hello, i'm Fish_Simple and my name is {name}",
        'say_energy': 100,
        'swim_out': f"My name is {name} and i swimming",
        'swim_energy': 95,
        'run_out': f"My name is {name} and i can't run",
        'run_energy': 100,
        'fly_out': f"My name is {name} and i can't fly",
        'fly_energy': 95,
    }

    checking(capfd, fish, expected)

def test_flying_fish(capfd):
    name = 'Lula'
    flying_fish = Fish_Can_Fly(name)

    expected = {
        'say_out': f"Hello, i'm Fish_Can_Fly and my name is {name}",
        'say_energy': 100,
        'swim_out': f"My name is {name} and i swimming",
        'swim_energy': 95,
        'run_out': f"My name is {name} and i can't run",
        'run_energy': 100,
        'fly_out': f"My name is {name} and i flying",
        'fly_energy': 75,
    }

    checking(capfd, flying_fish, expected)


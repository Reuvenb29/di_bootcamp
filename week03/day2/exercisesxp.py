# Exercise 1: Pets

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f"{self.name} is just walking around"

class Bengal(Cat):
    def sing(self, sounds):
        return f"{sounds}"

class Chartreux(Cat):
    def sing(self, sounds):
        return f"{sounds}"

class Siamese(Cat):
    def sing(self, sounds):
        return f"{sounds}"

# Making a few cats here
cat1 = Bengal("Simba", 3)
cat2 = Chartreux("Luna", 2)
cat3 = Siamese("Milo", 4)

# Putting them into a list for Sara
all_cats = [cat1, cat2, cat3]

# Giving all the cats to Sara as pets
sara_pets = Pets(all_cats)

# Time for a walk
sara_pets.walk()


# Exercise 2: Dogs

class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        self_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight

        if self_power > other_power:
            return f"{self.name} won the fight"
        elif self_power < other_power:
            return f"{other_dog.name} won the fight"
        else:
            return "It's a tie!"

# Trying it out with 3 dogs
dog1 = Dog("Rex", 5, 20)
dog2 = Dog("Buddy", 4, 18)
dog3 = Dog("Rocky", 6, 25)

print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog3))


# Exercise 3: PetDog class

import random

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        names = ', '.join([dog.name for dog in args])
        print(f"{self.name}, {names} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
            print(random.choice(tricks))
        else:
            print(f"{self.name} isn't trained yet!")

# Giving it a spin
dog1 = PetDog("Max", 3, 15)
dog2 = PetDog("Bella", 4, 18)
dog3 = PetDog("Charlie", 2, 10)

dog1.train()
dog1.play(dog2, dog3)
dog1.do_a_trick()


# Exercise 4: Family class

class Family():
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"Welcome to the family, {kwargs['name']}!")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False

    def family_presentation(self):
        print(f"Family: {self.last_name}")
        for member in self.members:
            print(member)

# Making a sample family
members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
]

my_family = Family("Smith", members)

my_family.family_presentation()
print(my_family.is_18("Michael"))
my_family.born(name='Tommy', age=0, gender='Male', is_child=True)
my_family.family_presentation()


# Exercise 5: The Awesomes Family (because why not have a little fun with it?)

class TheAwesomes(Family):
    def use_power(self, name):
        for member in self.members:
            if member['name'] == name:
                if member['age'] >= 18:
                    print(f"{member['name']}'s power is: {member['power']}")
                else:
                    raise Exception(f"Hold up! {member['name']} is not over 18 yet!")

    def awesome_presentation(self):
        print("Meet the one and only... Awesomes family!")
        super().family_presentation()

# Putting the crew together
awesome_members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'MindReader'}
]

awesomes = TheAwesomes("Awesomes", awesome_members)

awesomes.awesome_presentation()
awesomes.use_power("Michael")

# Time to add Baby Jack to the Awesomes
awesomes.born(name="Jack", age=1, gender="Male", is_child=True, power="Unknown Power", incredible_name="LilJack")
awesomes.awesome_presentation()

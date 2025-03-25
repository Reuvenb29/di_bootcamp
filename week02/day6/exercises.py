# --- Exercise 1 ---

# make a class called Cat
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# make 3 cats
cat1 = Cat("Kitty", 3)
cat2 = Cat("Tom", 5)
cat3 = Cat("Jerry", 2)

#find the oldest cat
def find_oldest_cat(cats):
    return max(cats, key=lambda cat: cat.age)

#print the oldest cat
oldest_cat = find_oldest_cat([cat1, cat2, cat3])
print(f"The oldest cat is {oldest_cat.name} and it is {oldest_cat.age} years old")

# --- Exercise 2
#  make a class called Dog
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")

# davids dog
davids_dog = Dog("Rex", 50)
print(f"David's dog is {davids_dog.name} and is {davids_dog.height} cm tall.")
davids_dog.bark()
davids_dog.jump()

# sarahs dog
sarahs_dog = Dog("Teacup", 20)
print(f"Sarah's dog is {sarahs_dog.name} and is {sarahs_dog.height} cm tall.")
sarahs_dog.bark()
sarahs_dog.jump()

# which dog is bigger
if davids_dog.height > sarahs_dog.height:
    print(f"The bigger dog is {davids_dog.name}.")
else:
    print(f"The bigger dog is {sarahs_dog.name}.")


# --- Exercise 3 ---
# make a class called Song
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

# create a song
stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()

# --- Exercise 4 ---
# make a class called Zoo
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print("Animals in the zoo:")
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        self.animals.sort()
        grouped = {}
        for animal in self.animals:
            first_letter = animal[0].upper()
            if first_letter in grouped:
                if isinstance(grouped[first_letter], list):
                    grouped[first_letter].append(animal)
                else:
                    grouped[first_letter] = [grouped[first_letter], animal]
            else:
                grouped[first_letter] = animal
        self.grouped_animals = grouped

    def get_groups(self):
        print("Animal groups:")
        for group, animals in self.grouped_animals.items():
            print(f"{group}: {animals}")

# make and use the zoo
new_york_zoo = Zoo("New York Zoo")
new_york_zoo.add_animal("Bear")
new_york_zoo.add_animal("Baboon")
new_york_zoo.add_animal("Cat")
new_york_zoo.add_animal("Cougar")
new_york_zoo.add_animal("Ape")
new_york_zoo.add_animal("Emu")
new_york_zoo.add_animal("Eel")

new_york_zoo.get_animals()

new_york_zoo.sell_animal("Bear")

new_york_zoo.sort_animals()
new_york_zoo.get_groups()
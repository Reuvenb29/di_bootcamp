#old macdonalds
class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, animal, amount=1):
        if animal in self.animals:
            self.animals[animal] += amount
        else:
            self.animals[animal] = amount

    def get_info(self):
        output = f"{self.name}'s farm\n\n"
        for animal, count in self.animals.items():
            output += f"{animal} : {count}\n"
        output += "\nE-I-E-I-0!"
        return output

    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        animal_list = self.get_animal_types()
        plural_animals = [animal + 's' for animal in animal_list]
        if len(plural_animals) > 1:
            last_animal = plural_animals.pop()
            animals_str = ", ".join(plural_animals) + f" and {last_animal}"
        else:
            animals_str = plural_animals[0]
        return f"{self.name}'s farm has {animals_str}."


#testibng
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

print(macdonald.get_info())
print("\n" + macdonald.get_short_info())
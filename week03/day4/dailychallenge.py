# --- Daily Challenge ---
import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius:
            self.radius = radius
        elif diameter:
            self.radius = diameter / 2
        else:
            raise ValueError("You must provide either a radius or a diameter.")

    @property
    def diameter(self):
        return self.radius * 2

    def area(self):
        return math.pi * (self.radius ** 2)

    def __str__(self):
        return f"Circle with radius: {self.radius}"

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        return NotImplemented

    def __eq__(self, other):
        return self.radius == other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __lt__(self, other):
        return self.radius < other.radius

# --- Testing the class ---
c1 = Circle(radius=4)
c2 = Circle(diameter=10)

print(c1)  # Circle with radius: 4
print("Radius:", c2.radius)  # 5.0
print("Diameter:", c1.diameter)  # 8
print("Area of c1:", round(c1.area(), 2))

# Adding circles
c3 = c1 + c2
print("New circle (c1 + c2):", c3)

# Comparisons
print("c1 == c2:", c1 == c2)
print("c1 > c2:", c1 > c2)

# Sorting circles
circles = [c2, c1, c3]
circles.sort()
print("Sorted circles by radius:")
for circle in circles:
    print(circle)

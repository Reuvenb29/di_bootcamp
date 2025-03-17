# Exercise 1: Hello World
print("Hello world\nHello world\nHello world\nHello world")

# Exercise 2: Some Math
result = (99 ** 3) * 8
print("Exercise 2 result:", result)

# Exercise 3: What is the Output?
print("Exercise 3 results:")
print(5 < 3)  # False
print(3 == 3)  # True
print(3 == "3")  # False
# print("3" > 3)  # This will cause an error, so we comment it out
print("Hello" == "hello")  # False

# Exercise 4: Your Computer Brand
computer_brand = "Lenovo"  # Replace with your actual computer brand
print(f"I have a {computer_brand} computer")

# Exercise 5: Your Information
name = "Reuven"  # Replace with your name
age = 25  # Replace with your age
shoe_size = 42  # Replace with your shoe size
info = f"My name is {name}, I am {age} years old, and my shoe size is {shoe_size}."
print(info)

# Exercise 6: A & B
a = 10
b = 5
if a > b:
    print("Hello World")

# Exercise 7: Odd or Even
num = int(input("Exercise 7 - Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Exercise 8: What’s Your Name?
my_name = "Reuven"  # Replace with your name
user_name = input("Exercise 8 - What is your name? ")
if user_name == my_name:
    print("Wow! We have the same name!")
else:
    print(f"Nice to meet you, {user_name}!")

# Exercise 9: Tall Enough to Ride?
height = int(input("Exercise 9 - Enter your height in cm: "))
if height >= 145:
    print("You are tall enough to ride!")
else:
    print("You need to grow some more to ride.")

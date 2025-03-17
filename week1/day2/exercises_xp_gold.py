# Exercise 1: Hello World - I Love Python
print("Hello world\nHello world\nHello world\nHello world\n"
      "I love python\nI love python\nI love python\nI love python")


# Exercise 2: What is the Season?

# Ask the user for a month (1 to 12)
month = int(input("Enter a month number (1-12): "))

# Determine the season based on the month
if month in [3, 4, 5]:
    season = "Spring"
elif month in [6, 7, 8]:
    season = "Summer"
elif month in [9, 10, 11]:
    season = "Autumn"
elif month in [12, 1, 2]:
    season = "Winter"
else:
    season = "Invalid month number"

# Print the result
print(f"The season is: {season}")

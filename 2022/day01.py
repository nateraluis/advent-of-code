import aocd

# Challenge: https://adventofcode.com/2022/day/1
# This list represents the Calories of the food carried by five Elves.
# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

data = aocd.get_data(day=1, year=2022)

elves_food = [[int(food) for food in elves.splitlines()] for elves in data.split("\n\n")]

print("Max food calories: ", max(sum(elf) for elf in elves_food))

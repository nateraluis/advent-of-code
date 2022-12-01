# Use a heap queue to find the three largest values
# https://en.wikipedia.org/wiki/Binary_heap
import heapq

import aocd

# Challenge: https://adventofcode.com/2022/day/1
# This list represents the Calories of the food carried by five Elves.
# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

data = aocd.get_data(day=1, year=2022)

elves_food = [[int(food) for food in elves.splitlines()] for elves in data.split("\n\n")]

# Part 1
print("Max food calories: ", max(sum(elf) for elf in elves_food))

# Part 2
# Find the three Elves who have the most Calories in their food, and sum their Calories.
# What is the total number of Calories that these three Elves have?


top_three = heapq.nlargest(3, elves_food, key=sum)

print("Total food calories: ", sum(sum(elf) for elf in top_three))

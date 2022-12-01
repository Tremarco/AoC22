# get data from the local txt file
with open('data.txt') as file:
    data = [i for i in file.read().strip().split("\n")]

# count calories of current elf here
calorie_counter = 0
# remember 3 highest totals
highest_calories = 0
highest_calories2 = 0
highest_calories3 = 0

for food in data:
    # if food is an empty string
    if food == "":
        # reset to 0
        calorie_counter = 0
    else:
        # cast to int and add to current elf's count
        calorie_counter += int(food)

    # set highest calories to calorie counter if it beats what is currently stored there
    if calorie_counter > highest_calories:
        highest_calories3 = highest_calories2
        highest_calories2 = highest_calories
        highest_calories = calorie_counter
    elif calorie_counter > highest_calories2:
        highest_calories3 = highest_calories2
        highest_calories2 = calorie_counter
    elif calorie_counter > highest_calories3:
        highest_calories3 = calorie_counter

print(f"Answer 1: {highest_calories}")
print(f"Answer 2: {highest_calories + highest_calories2 + highest_calories3}")








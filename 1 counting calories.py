with open('data.txt') as file:
    data = [i for i in file.read().strip().split("\n")]

calorie_counter = 0
highest_calories = 0

for food in data:
    if food != "":
        food_calories = int(food)
        calorie_counter += food_calories
    else:
        calorie_counter = 0

    if calorie_counter > highest_calories:
        highest_calories = calorie_counter

print(highest_calories)








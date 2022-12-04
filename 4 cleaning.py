# get data from local txt file
with open ('data.txt') as file:
    data = [i for i in file.read().strip().split("\n")]

# counter variables for answers
answer1 = 0
answer2 = 0

# iterate through each pair of elves
for pair in data:
    # split elf 1 and elf 2 using the comma
    elves = pair.split(",", 1)
    # new lists containing only the start room and finish room for each elf
    elf1 = elves[0].split("-", 1)
    elf2 = elves[1].split("-", 1)
    # get all ints between the ranges of each elf's start and finish rooms (+1 to the finish room as should be inclusive)
    elf1rooms = list(range(int(elf1[0]), int(elf1[1]) + 1))
    elf2rooms = list(range(int(elf2[0]), int(elf2[1]) + 1))

    # if every room is contained in the other elf's rooms, increment answer1
    if all(i in elf1rooms for i in elf2rooms):
        answer1 += 1
        print(elf1rooms, elf2rooms)
    elif all(i in elf2rooms for i in elf1rooms):
        answer1 += 1
        print(elf1rooms, elf2rooms)

    # loop through first elf rooms and check if ANY of those rooms appear in elf2's assignments
    # if so, increment answer2
    for room in elf1rooms:
        if room in elf2rooms:
            answer2 += 1
            break
# print answers
print(f"Answer 1 is {answer1}.\nAnswer 2 is {answer2}.")

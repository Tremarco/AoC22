# Read all data at once from local file
with open ("data.txt") as file:
    data = file.read()

# for every 4 steps of i in the range of data
for i in range(4, len(data)):
    # create a set from i-4 to i (doesn't allow duplicate values)
    group = set(data[(i - 4):i])
    # if the length of the set is 4, all 4 indexes preceding and including i are unique
    if len(group) == 4:
        # so print the answer
        print(f"Answer to part 1: {i}")
        break

# identical to part 1, just change all the 4s to 14s!
for i in range(14, len(data)):
    group = set(data[(i - 14):i])
    if len(group) == 14:
        print(f"Answer to part 2: {i}")
        break


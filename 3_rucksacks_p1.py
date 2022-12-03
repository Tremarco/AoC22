with open ('data.txt') as file:
    data = [i for i in file.read().strip().split("\n")]

upper_ascii_convert, lower_ascii_convert = -38, -96
sum = 0

for line in data:
    half = int(len(line) / 2)
    compartment1 = line[:half]
    compartment2 = line[half:]
    for char in compartment1:
        if char in compartment2:
            if char.isupper():
                sum += (ord(char) + upper_ascii_convert)
                break
            elif char.islower():
                sum += (ord(char) + lower_ascii_convert)
                break

print(sum)


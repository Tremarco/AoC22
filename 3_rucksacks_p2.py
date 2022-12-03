with open ('data.txt') as file:
    data = [i for i in file.read().strip().split("\n")]

upper_ascii_convert, lower_ascii_convert = -38, -96
sum = 0

for i in range(int(len(data))):
    if i % 3 == 0:
        group = data[i], data[i + 1], data[i + 2]
        for char in group[0]:
            if char in group[1] and char in group[2]:
                if char.isupper():
                    sum += (ord(char) + upper_ascii_convert)
                    break
                elif char.islower():
                    sum += (ord(char) + lower_ascii_convert)
                    break
print(sum)


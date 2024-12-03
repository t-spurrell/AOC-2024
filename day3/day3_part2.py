import re 

with open("day3\input.txt", "r") as file:
    data = file.read()

#print(data)
matches = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", data)
print(matches)
total = 0
skip = False
for match in matches:
    print('processing'  + match)
    if match == 'do()':
        skip = False
        continue
    elif match == "don't()":
        skip = True
    if skip:
        continue
    else:
        x, y = map(int, match[4:-1].split(","))
        total += x * y
print(total)
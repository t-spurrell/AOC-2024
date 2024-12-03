import re 
with open("day3\input.txt", "r") as file:
    data = file.read()

#print(data)
matches = re.findall(r"mul\(\d+,\d+\)", data)
total = 0
for match in matches:
    x, y = map(int, match[4:-1].split(","))
    total += x * y
print(total)

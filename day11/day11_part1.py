with open("day11\input.txt", "r") as file:
    data = file.read().split()
print(data)

for _ in range(75):
    total = []
    for d in data:
        if int(d) == 0:
            total.append(1)
        elif len(str(d)) % 2 == 0:
            d = str(d)
            length = len(d)
            total.append(int(d[:length//2]))
            total.append(int(d[length//2:]))
        else:
            total.append(int(d)*2024)
    data = total

print(len(data))

            

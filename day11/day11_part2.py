with open("day11\input.txt", "r") as file:
    data = file.read().split()
print(data)

stones = {}
for d in data:
    if d not in stones:
        stones[d] = 1

for _ in range(75):
    total = {}
    for stone, count in stones.items():
        if int(stone) == 0:
            if 1 not in total:
                total[1] = count
            else:
                total[1] += count
        elif len(str(stone)) % 2 == 0:
            stone = str(stone)
            length = len(stone)
            if int(stone[:length//2]) not in total:
                total[int(stone[:length//2])] = count
            else:
                total[int(stone[:length//2])] += count
            if int(stone[length//2:]) not in total:
                total[int(stone[length//2:])] = count
            else:
                total[int(stone[length//2:])] += count
        else:
            if int(stone)*2024 not in total:
                total[int(stone)*2024] = count
            else:
                total[int(stone)*2024] += count
    stones = total

print(sum(stones.values()))
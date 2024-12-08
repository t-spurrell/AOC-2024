with open("day8\input.txt", "r") as file:
    data = file.read().splitlines()
    #print(data)
    
rows = len(data)
cols = len(data[0])

antennas = {}
for r, row in enumerate(data):
    for c, char in enumerate(row):
        if char != ".":
            if char not in antennas:
                antennas[char] = []
            antennas[char].append((r, c))
#print(antennas)

antinodes = set()
for antenna_list in antennas.values():
    for i in range(len(antenna_list)):
        for j in range(i+1, len(antenna_list)):
            r1, c1 = antenna_list[i]
            r2, c2 = antenna_list[j]
            anti1 = (2*r2 - r1, 2*c2 - c1)
            anti2 = (2*r1 - r2, 2*c1 - c2)

            if 0 <= anti1[0] < rows and 0 <= anti1[1] < cols:
                antinodes.add(anti1)
            if 0 <= anti2[0] < rows and 0 <= anti2[1] < cols:
                antinodes.add(anti2)
print(len(antinodes))
      
        
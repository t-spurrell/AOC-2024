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
        for j in range(len(antenna_list)):
            if i == j:
                continue    
            r1, c1 = antenna_list[i]
            r2, c2 = antenna_list[j]
            new_r = r2 - r1
            new_c = c2 - c1
            r_start = r1
            c_start = c1
            while 0 <= r_start < rows and 0 <= c_start < cols:
                antinodes.add((r_start, c_start))
                r_start += new_r
                c_start += new_c
            
print(len(antinodes))
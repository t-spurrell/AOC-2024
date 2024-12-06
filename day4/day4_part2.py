with open("day4\input.txt", "r") as file:
    data = file.read().splitlines()

#print(data)
total = 0
for row in range(1, len(data) -1):
    for col in range(1, len(data[row]) -1):
        #print(data[row][col])
        if data[row][col].lower() != "a":
            continue
        edges = [data[row-1][col-1], data[row-1][col+1], data[row+1][col+1], data[row+1][col-1]]
        if edges[0].lower() == 'm' and edges[1].lower() == 'm' and edges[2].lower() == 's' and edges[3].lower() == 's':
            total += 1
        if edges[0].lower() == 'm' and edges[1].lower() == 's' and edges[2].lower() == 's' and edges[3].lower() == 'm':
            total += 1
        if edges[0].lower() == 's' and edges[1].lower() == 's' and edges[2].lower() == 'm' and edges[3].lower() == 'm':
            total += 1
        if edges[0].lower() == 's' and edges[1].lower() == 'm' and edges[2].lower() == 'm' and edges[3].lower() == 's':
            total += 1
        

print(total)
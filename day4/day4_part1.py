with open("day4\input.txt", "r") as file:
    data = file.read().splitlines()

#print(data)
total = 0
for row in range(len(data)):
    for col in range(len(data[row])):
        #print(data[row][col])
        if data[row][col].lower() != "x":
            continue
        for other_row, other_col in [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]:
         
            if not (0 <= row + 3 * other_row < len(data) and 0 <= col + 3 * other_col < len(data[row])):
                continue
            if data[row + other_row][col + other_col].lower() == "m" and data[row + 2 * other_row][col + 2 * other_col].lower() == "a" and data[row + 3 * other_row][col + 3 * other_col].lower() == "s":
                print(row, col)
                total += 1

print(total)
            
            
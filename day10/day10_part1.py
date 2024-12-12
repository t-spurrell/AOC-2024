with open("day10\input.txt", "r") as file:
    data = file.read().splitlines()
    data = list((map(list, data)))
    
rows = len(data)
cols = len(data[0])

zeros = [(row,col) for row in range(rows) for col in range(cols) if data[row][col] == "0"]

def trail_score(grid, row, col):
    queue = [(row, col)]
    reached = set()
    while queue:
        r, c = queue.pop(0)
        for next_r, next_c in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
            if next_r < 0 or next_c < 0 or next_r >= rows or next_c >= cols:
                continue
            if int(grid[next_r][next_c]) != int(grid[r][c]) +1:
                continue
            if grid[next_r][next_c] == "9":
                reached.add((next_r, next_c))
            else:
                queue.append((next_r, next_c))
    return reached

total = 0          
for row, col in zeros:
    total += len(trail_score(data, row, col))

print(total)
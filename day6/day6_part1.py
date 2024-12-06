with open("day6\input.txt", "r") as file:
    data = file.read().splitlines()
    

print(data)
#print(data[6][5])
for row in data:
    if '^' in row:
        starting_point = row.index('^'), data.index(row)
        break

print(starting_point) 

tracking = set()
start_r = starting_point[1]
start_c = starting_point[0]
other_row = -1
other_col = 0
           
while True:
    tracking.add((start_r, start_c))
    if start_r + other_row < 0 or start_r + other_row >= len(data) or start_c + other_col < 0 or start_c + other_col >= len(data[0]):
        break
    if data[start_r + other_row][start_c + other_col] == '#':
        #print('in here')
        other_col, other_row = -other_row, other_col
    else:
        #print(start_r, other_row)
        start_r += other_row
        start_c += other_col

print(len(tracking))

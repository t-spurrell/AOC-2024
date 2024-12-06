with open("day6\input.txt", "r") as file:
    #data = file.read().splitlines()
    data = list((map(list, file.read().splitlines())))
    # print(len(data))
    # print(len(data[0]))


#print(data)

for row in data:
    if '^' in row:
        starting_point = row.index('^'), data.index(row)
        break


# tracking = set()
print(starting_point)
start_r = starting_point[1]
start_c = starting_point[0]

def loop_check(data, start_r, start_c): 
    tracking = set() 
    other_row = -1
    other_col = 0        
    while True:
        tracking.add((start_r, start_c, other_row, other_col))
        if start_r + other_row < 0 or start_r + other_row >= len(data) or start_c + other_col < 0 or start_c + other_col >= len(data[0]):
            return False
        if data[start_r + other_row][start_c + other_col] == '#':
            #print('in here')
            other_col, other_row = -other_row, other_col
        else:
            #print(start_r, other_row)
            start_r += other_row
            start_c += other_col
        if (start_r, start_c, other_row, other_col) in tracking:
            return True

looped = 0

for row in range(len(data)):
    for col in range(len(data[0])):
        if data[row][col] != '.':
            continue
        data[row][col] = '#'
        if loop_check(data, start_r, start_c):
            looped += 1
        data[row][col] = '.'
print(looped)


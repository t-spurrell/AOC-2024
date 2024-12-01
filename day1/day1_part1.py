with open("day1\input.txt", "r") as file:
    data = file.read().splitlines()

x_list=[]
y_list=[]
for d in data:
    x,y = d.split()
    x_list.append(int(x))
    y_list.append(int(y))
x_list_sorted = sorted(x_list)
y_list_sorted = sorted(y_list)
zipped = zip(x_list_sorted, y_list_sorted)

distance = 0
for x,y in zipped:
    diff = y - x
    distance += abs(diff)
print(distance)
    
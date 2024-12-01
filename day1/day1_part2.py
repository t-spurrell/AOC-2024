with open("day1\input.txt", "r") as file:
    data = file.read().splitlines()

x_list=[]
y_list=[]
for d in data:
    x,y = d.split()
    x_list.append(int(x))
    y_list.append(int(y))

distance = 0
for x in x_list:
    repeated = y_list.count(x)
    distance += repeated*x
print(distance)
    
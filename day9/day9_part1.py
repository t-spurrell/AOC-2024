with open("day9\input.txt", "r") as file:
    data = file.read().strip()
    #print(len(data))

disks = [d for i, d in enumerate(data) if not i % 2] 
space = [s for i, s in enumerate(data) if i % 2]
#print(len(disks), len(space))
if len(disks) != len(space):
    space.append('x')
#print(len(disks), len(space))

f= []
for i, numbers in enumerate(zip(disks, space)):
    #print(numbers)
    file, size = numbers
    f += [i]*int(file)
    if size != 'x':
        f += ['.']*int(size)
#print(len(f))

dots = [i for i, x in enumerate(f) if x == '.']
#print(len(dots))

for dot in dots:
    #print(dot)
    while f[-1] == '.':
        f.pop()
    if len(f) <= dot:
        break
    f[dot] = f.pop()

total = 0
for i, x in enumerate(f):
    total += i*int(x)

print(total)



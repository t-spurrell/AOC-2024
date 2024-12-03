with open("day2\input.txt", "r") as file:
    data = file.read().splitlines()

def safe_checker(number_list:list):
    difference = [ int(x) - int(y) for x, y in zip(number_list, number_list[1:])]
    pos_status = []
    for d in difference:
        if 1<= d <=3:
            pos_status.append(True)
        else:
            pos_status.append(False)
            break
    neg_status = []
    for d in difference:
        if -1>= d >=-3:
            neg_status.append(True)
        else:
            neg_status.append(False)
            break
    return all(pos_status) or all(neg_status)

safe = 0
for d in data:
    numbers = d.split(" ")
    if safe_checker(numbers):
        safe += 1
    else:
        if any(safe_checker(numbers[:i] + numbers[i+1:]) for i in range(len(numbers))):
            safe += 1
print(safe)
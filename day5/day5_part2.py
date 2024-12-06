with open("day5\input.txt", "r") as file:
    rules = file.read().splitlines()

with open("day5\input2.txt", "r") as file:
    updates = file.read().splitlines()

rules = [rule.split("|") for rule in rules]
updates = [update.split(",") for update in updates]
#print(rules)
#print(updates)

def checker(update:list[str], rules):
    for rule in rules:
        x, y = rule
        #print(x, y)
        if x not in update and y not in update:
            continue
        elif x in update and y in update:
            if update.index(x) > update.index(y):
                return False
    return True

def correct_order(update:list[str], rules):
    for rule in rules:
        x, y = rule
        if x in update and y in update:
            if update.index(x) > update.index(y):
                update[update.index(x)] = y
                update[update.index(y)] = x
                correct_order(update, rules)
    return update
        

#total_updates = 0
mid_total = 0
new = []
for update in updates:
    #print(update)
    if not checker(update, rules):
        update = correct_order(update, rules)
        #print(update)
        new.append(update)
        mid = update[len(update)//2]
        mid_total += int(mid)         

#print(total_updates)
print(mid_total)
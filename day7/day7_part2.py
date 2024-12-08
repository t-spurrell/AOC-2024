with open("day7\input.txt", "r") as file:
    data = file.read().splitlines()

new_data = [d.split(':') for d in data]

def possible(current_val, target_val, numbers, index):
    if index == len(numbers):
        if current_val == int(target_val):
            return True
        else:
            return False
        
    add = possible(int(current_val) + int(numbers[index]), target_val, numbers, index + 1)
    multiply = possible(int(current_val) * int(numbers[index]), target_val, numbers, index + 1)
    concat = possible(int(str(current_val) + str(numbers[index])), target_val, numbers, index + 1)
    if add or multiply or concat:
        return True

answer = 0
for target_val, numbers in new_data:
    numbers = numbers.split()
    #print(numbers)
    current_val = int(numbers[0])
    if possible(current_val, target_val, numbers, 1):
        answer += int(target_val)
            
print(answer)
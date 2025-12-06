import time
from math import prod

def operate(operands, operator):
    operator = sum if operator == '+' else prod
    return operator(operands)

def part_1(input_data):
    nums = []
    operators = []
    for line in input_data:
        line = line.rstrip()
        if line[0].isdigit() or line[0] == ' ':
            nums.append([ int(num) for num in line.split() ])
        else:
            operators = line.split()
    
    operands = []
    for i in range(len(nums[0])):
        operands.append([line[i] for line in nums])
    result = list(map(operate, operands, operators))
    
    return sum(result)

def part_2(input_data):
    operands = [[]]
    operators = []
    for i in range(len(input_data[0]) - 1): # -1 for \n
        if input_data[-1][i] != ' ':
            operators.append(input_data[-1][i])
        if all([line[i] == ' ' for line in input_data]):
            operands.append([])
        else:
            num = ""
            for j in input_data[:-1]:
                if j[i] != ' ':
                    num += j[i]
            operands[-1].append(int(num))
    
    result = list(map(operate, operands, operators))
    
    return sum(result)

def main():
    test_input_file = "2025/input/day_6_test_input.txt"
    with open(test_input_file) as f:
        test_input = f.readlines()

    day_input_file = "2025/input/day_6_input.txt"
    with open(day_input_file) as f:
        day_input = f.readlines()
    
    print(f"Test Output Part 1: {part_1(test_input)}")
    print(f"Day Output Part 1: {part_1(day_input)}")
    print(f"Test Output Part 2: {part_2(test_input)}")
    print(f"Day Output Part 2: {part_2(day_input)}")

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    duration = end_time - start_time
    print(f"Time taken: {duration} seconds")

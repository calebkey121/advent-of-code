import time

# 434 too low
def part_1(input_data):
    lines = [ line.strip() for line in input_data ]
    curr = 50
    zeros = 0
    for instruction in lines:
        direction, clicks = instruction[0], int(instruction[1:])
        if direction == 'L':
            clicks = -clicks
        curr += clicks
        if curr < 0:
            curr = 100 - abs(curr) % 100
        if curr > 99:
            curr %= 100
        if curr == 0:
            zeros += 1
    return zeros

# 7154 too high
# 7132 too high
def part_2(input_data):
    lines = [ line.strip() for line in input_data ]
    curr = 50
    zeros = 0
    for instruction in lines:
        direction, clicks = instruction[0], int(instruction[1:])
        if direction == 'L':
            clicks = -clicks
        curr += clicks
        if curr < 0:
            # need a slight adjustment if we started on zero vs moved past zero
            start_on_zero = 1
            if curr - clicks == 0:
                start_on_zero = 0
            zeros += start_on_zero + abs(curr) // 100
            curr = curr % 100
        elif curr > 99:
            zeros += curr // 100
            curr %= 100
        elif curr == 0:
            zeros += 1
    return zeros

def main():
    test_input_file = "2025/input/day_1_test_input.txt"
    with open(test_input_file) as f:
        test_input = f.readlines()

    day_input_file = "2025/input/day_1_input.txt"
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

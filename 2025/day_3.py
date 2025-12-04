import time

def part_1(input_data):
    joltages = []
    for bank in input_data:
        bank = bank.rstrip()
        first = max(bank[:-1])
        first_index = bank.index(first)
        second = max(bank[first_index + 1:])
        joltages.append(int(first + second))
    return sum(joltages)


def part_2(input_data):
    joltages = []
    num_digits = 12
    for bank in input_data:
        bank = bank.rstrip()

        prev_idx = 0
        digits = []
        for i in range(num_digits - 1, -1, -1):
            bank_slice = bank[prev_idx:-i] if i != 0 else bank[prev_idx:]
            digit = max(bank_slice)
            prev_idx += bank_slice.index(digit) + 1
            digits.append(digit)
        joltages.append(int(''.join(digits)))
    return sum(joltages)

def main():
    test_input_file = "2025/input/day_3_test_input.txt"
    with open(test_input_file) as f:
        test_input = f.readlines()

    day_input_file = "2025/input/day_3_input.txt"
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

import time

def part_1(input_data):
    flip = False
    ranges = []
    ids = []
    for line in input_data:
        line = line.strip()
        if not line:
            flip = True
        elif not flip:
            ranges.append([int(a) for a in line.split('-')])
        else:
            ids.append(int(line))
    
    ranges = sorted(ranges, key=lambda x: x[0])
    num_fresh = 0
    for id in ids:
        spoiled = True
        for r in ranges:
            if id < r[0]:
                break
            elif id <= r[1]:
                spoiled = False
                break
        if not spoiled:
            num_fresh += 1

    return num_fresh
# part 1: 975 too high
# 299 too low

def merge(range_a, range_b):
    # returns two lists in order if no overlap, one list if overlap
    a, b = (range_a, range_b) if range_a[0] < range_b[0] else (range_b, range_a) # flip if range_b starts before range_a
    low_a, high_a, low_b, high_b = *a, *b
    if high_a < low_b:
        return a, b
    return [low_a, max(high_a, high_b)]

def insert(range_a, i, ranges):
    if range_a == []:
        return ranges
    if i == len(ranges):
        return [range_a]
    range_b = ranges[i]
    merged = merge(range_a, range_b)
    if range_a == merged[0]:
        return [range_a] + ranges[i:]
    elif range_b == merged[0]:
        return [range_b] + insert(range_a, i + 1, ranges)
    else: # merged into one
        return insert(merged, i + 1, ranges)
def part_2(input_data):
    flip = False
    ranges = []
    ids = []
    for line in input_data:
        line = line.strip()
        if not line:
            flip = True
        elif not flip:
            ranges.append([int(a) for a in line.split('-')])
        else:
            ids.append(int(line))
    
    # Condense the ranges
    merged_ranges = [ranges[0]]
    for a in ranges[1:]:
        merged_ranges = insert(a, 0, merged_ranges)

    possible_fresh = 0
    for r in merged_ranges:
        possible_fresh += r[1] - r[0] + 1

    return possible_fresh

def main():
    test_input_file = "2025/input/day_5_test_input.txt"
    with open(test_input_file) as f:
        test_input = f.readlines()

    day_input_file = "2025/input/day_5_input.txt"
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

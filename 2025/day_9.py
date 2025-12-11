import time
from itertools import combinations
from math import inf

def in_range(val, tup_range):
    return val >= tup_range[0] and val <= tup_range[1]

def valid(a, b, col_range, row_range):
    min_col, max_col = min(a[0], b[0]), max(a[0], b[0])
    min_row, max_row = min(a[1], b[1]), max(a[1], b[1])
    for i in range(min_col, max_col + 1):
        if not in_range(min_row, col_range[i]) or not in_range(max_row, col_range[i]):
            return False
    for i in range(min_row, max_row + 1):
        if not in_range(min_col, row_range[i]) or not in_range(max_col, row_range[i]):
            return False
    return True

def rect_area(a, b):
        return (abs(a[1] - b[1]) + 1) * (abs(a[0] - b[0]) + 1)

def part_1(input_data):
    red_tiles = [tuple(int(a) for a in line.strip().split(',')) for line in input_data]
    combos = list(combinations(red_tiles, 2))
    max_area = 0
    for combo in combos:
        if (area :=rect_area(*combo)) > max_area:
            max_area = area
    return max_area

def part_2(input_data):
    red_tiles = [tuple(int(a) for a in line.strip().split(',')) for line in input_data]

    # add green tiles (actaully a range of highest/lowest red or green tile)
    row_range = {}
    col_range = {}

    # add end to start just for tracing green tiles
    for r1, r2 in zip([red_tiles[-1]] + red_tiles, red_tiles):
        i = 1 if r1[0] == r2[0] else 0
        low, high = (r1[i], r2[i]) if r1[i] < r2[i] else (r2[i], r1[i])
        if i: # i == 1, 
            green_tiles = [(r1[0], row) for row in range(low + 1, high)]
        else: # i == 0
            green_tiles = [(col,r1[1]) for col in range(low + 1, high)]
        for a in [r1] + green_tiles:
            if a[0] not in col_range:
                col_range[a[0]] = [inf, -1]
            if a[1] not in row_range:
                row_range[a[1]] = [inf, -1]
            if a[1] < col_range[a[0]][0]:
                col_range[a[0]][0] = a[1]
            if a[1] > col_range[a[0]][1]:
                col_range[a[0]][1] = a[1]
            if a[0] < row_range[a[1]][0]:
                row_range[a[1]][0] = a[0]
            if a[0] > row_range[a[1]][1]:
                row_range[a[1]][1] = a[0]

    combos = list(combinations(red_tiles, 2))
    max_area = 0
    length = len(combos)
    for i, combo in enumerate(combos):
        if (area :=rect_area(*combo)) > max_area and valid(*combo, col_range, row_range):
            max_area = area
        print(f'{i}/{length}')
    return max_area

def main():
    test_input_file = "2025/input/day_9_test_input.txt"
    with open(test_input_file) as f:
        test_input = f.readlines()

    day_input_file = "2025/input/day_9_input.txt"
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

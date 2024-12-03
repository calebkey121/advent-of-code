import time
from enum import Enum, auto

def record_is_safe(record):
    direction = None
    for i, j in zip(record, record[1:]):
        diff = j - i # positive for increase, nevagive for decrease, 0 is right out
        if diff == 0 or abs(diff) > 3: # both of these invalidate
            return False
        if diff > 0: # increasing
            if direction is None: # first time sets direction
                direction = True
            if direction is False:
                # means we changed direction
                return False
        else: # decreasing
            if direction is None: # first time sets direction
                direction = False
            if direction is True:
                return False
    return True

def star_1():
    input_file = "2024/test_input/day_2_input.txt"
    # 594 too high
    with open(input_file) as f:
        lines = f.readlines()
        total_valid = 0
        for line in lines:
            record = [ int(num) for num in line.split() ]
            valid = record_is_safe(record)
            if valid:
                total_valid += 1
        return total_valid

class DiffType(Enum):
    INCREASING = auto()
    DECREASING = auto()
    EQUAL = auto()
    LARGE = auto()

def diff_type(a, b):
    diff = b - a
    if abs(diff) > 3:
        return DiffType.LARGE
    elif diff == 0:
        return DiffType.EQUAL
    elif diff > 0:
        return DiffType.INCREASING
    else:
        return DiffType.DECREASING

def is_safe(record):
    safe = True

    diffs = []
    diff_counts = {
        DiffType.INCREASING: 0,
        DiffType.DECREASING: 0,
        DiffType.LARGE: 0,
        DiffType.EQUAL: 0,
    }
    for i, j in zip(record, record[1:]):
        diff = diff_type(i, j)
        # print(f"i: {i}, j: {j}, diff: {diff}")
        diffs.append(diff)
        diff_counts[diff] += 1
    minority = DiffType.INCREASING if diff_counts[DiffType.INCREASING] < diff_counts[DiffType.DECREASING] else DiffType.DECREASING
    direction = DiffType.INCREASING if minority == DiffType.DECREASING else DiffType.DECREASING
    minority_count = diff_counts[minority]
    # necessarily unsafe if bad count is greater than 1
    if any( val > 1 for val in [ diff_counts[DiffType.EQUAL], diff_counts[DiffType.LARGE], minority_count ] ):
        return False
    # can only have one equal issue, or a large and minority issue, side by side
    if diff_counts[DiffType.EQUAL] + diff_counts[DiffType.LARGE] + minority_count > 2:
        return False
    
    #print(f"original record: {record}")
    #print(f"diffs: {diffs}")
    for index, diff in enumerate(diffs):
        if diff != direction:
            # check if slicing out either index works
            without_first = record[:index] + record[index + 1:]
            without_second = record[:index + 1] + record[index + 2:]
            #print(f"without first: {without_first}")
            #print(f"without second: {without_second}")
            safe = record_is_safe(without_first) or record_is_safe(without_second)
    #print(f"safe: {safe}")
    return safe

# checks if at a certain index, we could remove a number and still go in the right direction
def can_remove_one(record, index, direction):
    return False

def star_2():
    input_file = "2024/input/day_2_input.txt"
    num_safe = 0

    with open(input_file) as f:
        lines = f.readlines()
        for line in lines:
            record = [ int(num) for num in line.split() ]
            if is_safe(record):
                num_safe += 1
    
    print(num_safe)



if __name__ == "__main__":
    start_time = time.time()
    star_2()
    end_time = time.time()
    duration = end_time - start_time
    print(f"Time taken: {duration} seconds")

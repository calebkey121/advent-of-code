import time

def part_1(input_data):
    ranges = input_data[0].split(',')
    invalid_ids = []
    for r in ranges:
        beg, end = [ int(a) for a in r.split('-') ]
        for i in range(beg, end + 1):
            id = str(i)
            if id[:len(id) // 2] == id[len(id) // 2:]:
                invalid_ids.append(id)
    return sum([int(a) for a in invalid_ids])

def part_2(input_data):
    ranges = input_data[0].split(',')
    invalid_ids = []
    for r in ranges:
        beg, end = [ int(a) for a in r.split('-') ]
        for i in range(beg, end + 1):
            id = str(i)
            # start with 1 up to len(id) // 2
            for check_len in range(1, (len(id) // 2) + 1):
                if len(id) % check_len != 0:
                    continue # not possible for uneven split
                # split into equal parts of length check_len
                splits = [id[i * check_len: (i * check_len) + check_len ] for i in range(len(id) // check_len)]
                # check if all parts are equal (eqivalent to checking if all are equal to the first part)
                if all(i == splits[0] for i in splits[1:]):
                    invalid_ids.append(id)
                    break
    return sum([int(a) for a in invalid_ids])

def main():
    test_input_file = "2025/input/day_2_test_input.txt"
    with open(test_input_file) as f:
        test_input = f.readlines()

    day_input_file = "2025/input/day_2_input.txt"
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

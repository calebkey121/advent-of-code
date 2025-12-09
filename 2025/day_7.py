import time

def part_1(input_data):
    beams = set([input_data[0].find('S')])
    splits = 0
    for line in input_data[1:]:
        start = 0
        new_beams = set()
        while True:
            splitter = line.find('^', start)
            if splitter == -1:
                break
            start = splitter + 1
            # ensure beam is above splitter
            if splitter not in beams:
                continue
            # split happens
            beams.remove(splitter)
            splits += 1
            new_beams.update([splitter - 1, splitter + 1])
        beams.update(new_beams)
    return splits
# 970 too low

def part_2(input_data):
    beams = {input_data[0].find('S'): 1}
    for line in input_data[1:]:
        start = 0
        while True:
            splitter = line.find('^', start)
            if splitter == -1:
                break
            start = splitter + 1
            # ensure beam is above splitter
            if splitter not in beams:
                continue
            # split happens
            if splitter - 1 not in beams:
                beams[splitter - 1] = 0
            beams[splitter - 1] += beams[splitter]
            if splitter + 1 not in beams:
                beams[splitter + 1] = 0
            beams[splitter + 1] += beams[splitter]
            del beams[splitter]
    return sum([beams[a] for a in beams.keys()])

def main():
    test_input_file = "2025/input/day_7_test_input.txt"
    with open(test_input_file) as f:
        test_input = f.readlines()

    day_input_file = "2025/input/day_7_input.txt"
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

import time
from itertools import combinations
from math import dist

def part_1(input_data):
    junction_boxes = [tuple(int(a) for a in line.strip().split(',')) for line in input_data]
    combos = list(combinations(junction_boxes, 2))
    combos = sorted(combos, key=lambda x: dist(x[0], x[1]))
    circuits = [set([*combos[0]])]
    for combo in combos[1:1000]:
        a, b = combo
        added = False
        for i, circuit in enumerate(circuits):
            if a in circuit or b in circuit:
                check = b if a in circuit else a
                circuit.update([*combo])
                added = True

                # check remaining circuits for merging
                for j, check_circuit in enumerate(circuits[i + 1:]):
                    if check in check_circuit:
                        # merge the two
                        circuit.update(check_circuit)
                        del circuits[i + 1 + j]
                        break
                break
        if not added:
            circuits.append(set([*combo]))
    
    lengths = sorted([len(a) for a in circuits])


    return lengths[-1] * lengths[-2] * lengths[-3]
# 3864 too low, 36936 too low, incorrect 225720,37584

def part_2(input_data):
    junction_boxes = [tuple(int(a) for a in line.strip().split(',')) for line in input_data]
    combos = list(combinations(junction_boxes, 2))
    combos = sorted(combos, key=lambda x: dist(x[0], x[1]))
    circuits = [set([*combos[0]])]
    junction_boxes.remove(combos[0][0])
    junction_boxes.remove(combos[0][1])
    return_val = 0
    for combo in combos[1:]:
        a, b = combo
        if a in junction_boxes:
            junction_boxes.remove(a)
        if b in junction_boxes:
            junction_boxes.remove(b)
        added = False
        for i, circuit in enumerate(circuits):
            if a in circuit or b in circuit:
                check = b if a in circuit else a
                circuit.update([*combo])
                added = True

                # check remaining circuits for merging
                for j, check_circuit in enumerate(circuits[i + 1:]):
                    if check in check_circuit:
                        # merge the two
                        circuit.update(check_circuit)
                        del circuits[i + 1 + j]
                        break
                break
        if not added:
            circuits.append(set([*combo]))
        if len(circuits) == 1 and junction_boxes == []:
            return a[0] * b[0]


    return return_val

def main():
    test_input_file = "2025/input/day_8_test_input.txt"
    with open(test_input_file) as f:
        test_input = f.readlines()

    day_input_file = "2025/input/day_8_input.txt"
    with open(day_input_file) as f:
        day_input = f.readlines()
    
    #print(f"Test Output Part 1: {part_1(test_input)}")
    print(f"Day Output Part 1: {part_1(day_input)}")
    print(f"Test Output Part 2: {part_2(test_input)}")
    print(f"Day Output Part 2: {part_2(day_input)}")

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    duration = end_time - start_time
    print(f"Time taken: {duration} seconds")

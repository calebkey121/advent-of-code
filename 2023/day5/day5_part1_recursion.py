#!/usr/bin/python3

import time

MAPPING = {}
LEVELS = []

# Takes a value and its current level and travels up the mapping
# returns what seed would have resulted in that value
def travelUp(value, level):
    if level == 0:
        return value
    
    # find a mapping in current level if it exists
    foundMapping = False
    for mappy in MAPPING[LEVELS[level]]:
        source, dest, addl = mappy # We're traveling up, source dest are flipped from instructions
        if value in range(source, source + addl):
            diff = value - source
            foundMapping = True
            break

    if foundMapping:
        seed = travelUp(dest + diff, level - 1)
    else:
        seed = travelUp(value, level - 1)

    return seed

def main():
    input_file = "test.txt"

    with open(input_file) as f:
        lines = [ line.rstrip("\n") for line in f.readlines() if line != '\n']

        for line in lines:
            if "seeds" in line:
                MAPPING["seeds"] = [ int(seed) for seed in line.split(': ')[1].split() ]
            elif " map:" in line:
                key = line.rstrip(':')
                MAPPING[key] = []
            else:
                MAPPING[key].append([ int(num) for num in line.split() ])

        LEVELS.extend(list(MAPPING))
        
        # yeah if no seeds exist this wont work i get it
        location = 0
        while True:
            seed = travelUp(location, level=7)
            if seed in MAPPING["seeds"]:
                print(location)
                break
            else:
                location += 1


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    duration = end_time - start_time
    print(f"Time taken: {duration} seconds")
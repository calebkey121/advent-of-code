#!/usr/bin/python3

import time

def main():
    input_file = "test.txt"

    with open(input_file) as f:
        lines = [ line.rstrip("\n") for line in f.readlines() if line != '\n']

        mapping = {}
        for line in lines:
            if "seeds" in line:
                mapping["seeds"] = [ int(seed) for seed in line.split(': ')[1].split() ]
            elif " map:" in line:
                key = line.rstrip(':')
                mapping[key] = []
            else:
                mapping[key].append([ int(num) for num in line.split() ])

        print(mapping)

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    duration = end_time - start_time
    print(f"Time taken: {duration} seconds")
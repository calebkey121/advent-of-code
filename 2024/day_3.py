import time
import re

def star_1():
    input_file = "2024/input/day_3_input.txt"
    # 23943098, too low
    # 155955228, correct!
    with open(input_file) as f:
        lines = f.readlines()
        total = 0
        for line in lines:
            mul_pattern = r"mul\((\d+),(\d+)\)"
            matches = re.finditer(mul_pattern, line)
            for command in matches:
                # match lets compute the multiplication and continue
                first = int(command.group(1))
                second = int(command.group(2))
                print(f"found mul({first},{second})")
                total += first * second
        print(total)

def star_2():
    # 100189366
    input_file = "2024/input/day_3_input.txt"
    do = True
    with open(input_file) as f:
        lines = f.readlines()
        total = 0
        for line in lines:
            mul_pattern = r"mul\((\d+),(\d+)\)"
            do_pattern = r"do\(\)"
            dont_pattern = r"don't\(\)"
            patterns = rf"{mul_pattern}|({do_pattern})|({dont_pattern})"
            matches = re.findall(patterns, line)
            print(matches)
            for command in matches:
                if command[2]:
                    do = True
                elif command[3]:
                    do = False
                else:
                    first = int(command[0])
                    second = int(command[1])
                    if do:
                        print(f"doing mul({first}, {second})   (total: {total})")
                        total += first * second
                    else:
                        print(f"skipping mul({first}, {second})")
            print("\nend of line\n")

        print(total)

if __name__ == "__main__":
    start_time = time.time()
    star_2()
    end_time = time.time()
    duration = end_time - start_time
    print(f"Time taken: {duration} seconds")

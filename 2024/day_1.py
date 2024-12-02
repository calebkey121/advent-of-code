import time

def main():
    input_file = "2024/input/day_1_input.txt"

    with open(input_file) as f:
        lines = f.readlines()
        left_list, right_list = [], []
        for line in lines:
            left, right = line.split()
            left_list.append(int(left))
            right_list.append(int(right))

    left_list, right_list = sorted(left_list), sorted(right_list)    
    total = 0
    for l, r in zip(left_list, right_list):
        print(f"{l} - {r} = {l - r}")
        total += abs(l - r)
    print(total)


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    duration = end_time - start_time
    print(f"Time taken: {duration} seconds")

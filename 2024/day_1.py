import time

def star_1():
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

def main():
    input_file = "2024/input/day_1_input.txt"

    with open(input_file) as f:
        lines = f.readlines()
        left_list, right_list = [], []
        for line in lines:
            left, right = line.split()
            left_list.append(int(left))
            right_list.append(int(right))

    similarity_score = {}
    for l in left_list:
        similarity_score[l] = 0
    
    for r in right_list:
        if r in similarity_score:
            similarity_score[r] += 1
    
    score = 0
    for l in left_list:
        score += l * similarity_score[l]
    print(score)


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    duration = end_time - start_time
    print(f"Time taken: {duration} seconds")

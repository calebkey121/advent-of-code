import time

def main():
    input_file = "input/day_1_input.txt"

    with open(input_file) as f:
        lines = f.readlines()

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    duration = end_time - start_time
    print(f"Time taken: {duration} seconds")

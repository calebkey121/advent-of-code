def main():
    input_file = "day6_input.txt"

    with open(input_file) as f:

        lines = f.readlines()

        
        
        race_time = int(lines[0].split(':')[1].replace(" ", ""))
        target_distance = int(lines[1].split(':')[1].replace(" ", ""))
        
        total = 0

        hold_time = 1
        while hold_time < race_time:
            speed = hold_time
            elapsed_time = race_time - hold_time
            distance = speed * elapsed_time

            if distance > target_distance:
                total += 1
            hold_time += 1
        print(total)



if __name__ == "__main__":
    main()
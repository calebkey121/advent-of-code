def main():
    input_file = "day6_input.txt"

    with open(input_file) as f:

        lines = f.readlines()

        
        
        times = [ int(num) for num in lines[0].split(':')[1].split() ]
        distances = [ int(num) for num in lines[1].split(':')[1].split() ]
        
        totals = []
        for race in range(len(times)):
            total = 0
            race_time = times[race]
            target_distance = distances[race]

            hold_time = 1
            while hold_time < race_time:
                speed = hold_time
                elapsed_time = race_time - hold_time
                distance = speed * elapsed_time

                if distance > target_distance:
                    total += 1
                hold_time += 1
            totals.append(total)
        print(totals[0] * totals[1] * totals[2] * totals[3])



if __name__ == "__main__":
    main()
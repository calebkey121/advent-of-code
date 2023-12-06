import time

def main():
    input_file = "day5_input.txt"

    with open(input_file) as f:
        lines = [ line.rstrip("\n") for line in f.readlines() if line != '\n']

        source = []
        dest = []
        for line in lines:
            if "seeds" in line:
                dest = [ int(seed) for seed in line.split(': ')[1].split() ] # this will go to source when "seed-to-soil map:" executes in elif
            elif " map:" in line:
                if source:
                    dest.extend(source) # everything left in source had no mapping, pass it to destination
                source = dest
                dest = []
            else: # else we have destination, source, number describing additional times that is repeated
                dst, src, addl = [ int(rule) for rule in line.split() ]
                oldSource = source[:]
                for num in oldSource:
                    if num < src + addl and num >= src:
                        dest.append(dst + (num - src))
                        source.remove(num)

        # elif doesn't execute for "humidity-to-location map:" execute one last time
        if source:
            dest.extend(source) # everything left in source had no mapping, pass it to destination

        print(dest)
        print(min(dest))

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    duration = end_time - start_time
    print(f"Time taken: {duration} seconds")
import time

def main():
    input_file = "day9_input.txt"

    with open(input_file) as f:
        lines = f.readlines()

        total = 0
        for line in lines:
            oasis = []
            oasis.append([ int(val) for val in line.split() ])

            allZeros = False
            i = 0
            while not allZeros:
                diffs = []
                allZeros = True
                for j in range(len(oasis[i]) - 1):
                    diff = oasis[i][j + 1] - oasis[i][j]
                    if diff != 0:
                        allZeros = False
                    diffs.append(diff)
                oasis.append(diffs)
                i += 1

            oasis = oasis[::-1]
            for level in range(len(oasis) - 1):
                oasis[level + 1].insert(0, oasis[level + 1][0] - oasis[level][0])
            print(oasis)

            total += oasis[-1][0]
        print(total)
            


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    duration = end_time - start_time
    print(f"Time taken: {duration} seconds")
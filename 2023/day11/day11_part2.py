import time

# too low 82000210

# a and b are tuples of two ints
# return number of steps
# if youre crossing an empty row or col, add 1000000 to the number of steps
def shortestPath(a, b, emptyRows, emptyCols):
    steps = abs(a[0] - b[0]) + abs(a[1] - b[1])

    expansion = 1000000
    
    for row in emptyRows:
        if row in range(min(a[0], b[0]), max(a[0], b[0])):
            steps += expansion - 1
    for col in emptyCols:
        if col in range(min(a[1], b[1]), max(a[1], b[1])):
            steps += expansion - 1

    return steps


def main():
    input_file = "day11_input.txt"

    with open(input_file) as f:
        lines = [ line.rstrip() for line in f.readlines() ]

        emptyRows = []
        for row in range(len(lines)):
            if lines[row] == '.' * len(lines[row]):
                emptyRows.append(row)

        emptyCols = []
        for col in range(len(lines[0])):
            dots = True
            for row in lines:
                if row[col] != '.':
                    dots = False
                    break
            if dots:
                emptyCols.append(col)

        # Expandings not needed
        galaxies = []
        for row in range(len(lines)):
            for col in range(len(lines[0])):
                if lines[row][col] == '#':
                    galaxies.append((row, col))

        total = 0
        for a in galaxies[:-1]:
            ind = galaxies.index(a) + 1
            for b in galaxies[ind:]:
                total += shortestPath(a, b, emptyRows, emptyCols)

        print(total)


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    duration = end_time - start_time
    print(f"Time taken: {duration} seconds")
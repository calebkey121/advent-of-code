import time

# a and b are tuples of two ints
# return number of steps
def shortestPath(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


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

        expanded = []
        for row in range(len(lines)):
            expandedRow = ""
            prevCol = 0
            for col in emptyCols:
                expandedRow += lines[row][prevCol:col] + '..'
                prevCol = col + 1
            expandedRow += lines[row][prevCol:]
            expanded.append(expandedRow)

        for row in emptyRows[::-1]:
            expanded.insert(row, '.' * len(expanded[0]))

        # Expandings Finished
        galaxies = []
        for row in range(len(expanded)):
            for col in range(len(expanded[0])):
                if expanded[row][col] == '#':
                    galaxies.append((row, col))

        total = 0
        for a in galaxies[:-1]:
            ind = galaxies.index(a) + 1
            for b in galaxies[ind:]:
                total += shortestPath(a, b)

        print(total)


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    duration = end_time - start_time
    print(f"Time taken: {duration} seconds")
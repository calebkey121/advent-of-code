import time

def main():
    input_file = "input.txt"

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

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    duration = end_time - start_time
    print(f"Time taken: {duration} seconds")
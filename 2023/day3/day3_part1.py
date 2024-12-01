# List of symbols: {'%', '\n', '&', '/', '#', '*', '-', '$', '=', '+', '@'}
FOUND_NUMBERS = {} # Newly discovered numbers are added as ()

def check_surroundings(lines, row, col):
    cells_to_check = [
        (row - 1, col - 1),
        (row - 1, col),
        (row - 1, col + 1),
        (row, col - 1),
        (row, col + 1),
        (row + 1, col - 1),
        (row + 1, col),
        (row + 1, col + 1),        
    ]
    valid_cells = [(r, c) for r, c in cells_to_check if 0 <= r <= len(lines) - 1 and 0 <= c <= len(lines[r]) - 1]

    # Check for digits in the valid cells
    found_digits = []
    for cell in valid_cells:
        value = lines[cell[0]][cell[1]]
        if value.isdigit():
            found_digits.append(cell)

    # There may be adjacent digits, which would be part of the same number and would be redundant. Lets remove adjacent found digits
    found_unique_digits = []
    for cell in found_digits:
        if (cell[0], cell[1] - 1) not in found_unique_digits:
            found_unique_digits.append(cell)

    # Check for surrounding digits in the ones found and construct the corresponding number
    found_numbers = []
    for cell in found_unique_digits:
        r = cell[0]
        c = cell[1]
        # loop to the right to find the least significant digit
        i = c
        while i + 1 < (len(lines[r])) and lines[r][(i + 1)].isdigit(): # while in bounds and next cell is digit
            i += 1
        
        # i is now at least significant digit, now loop to the left and build our number 
        number = 0
        significance = 0
        coords = [] # Coords will compare against 
        while i >= 0 and lines[r][i].isdigit():
            coords.append((r, i))
            number += int(lines[r][i]) * 10 ** significance
            significance += 1
            i -= 1
        
        # We've built our number, now check if its been found before
        if number not in FOUND_NUMBERS or FOUND_NUMBERS[number] != coords:
            FOUND_NUMBERS[number] = coords
            found_numbers.append(number)

    return found_numbers

def main():
    input_file = "day3_input.txt"
    with open(input_file) as f:
        lines = [line.rstrip('\n') for line in f.readlines()]

        symbols = []
        total = 0
        for row, line in enumerate(lines):
            for col, char in enumerate(line):
                # Find Symbol
                if not char.isdigit() and char != '.':
                    # Symbol Found
                    symbol = (row, col, char)
                    symbols.append(symbol)
                    
                    # Find numbers
                    found_numbers = check_surroundings(lines, row, col)
                    if found_numbers:
                        total += sum(found_numbers)

        print(total)
                        
                    





if __name__ == "__main__":
    main()
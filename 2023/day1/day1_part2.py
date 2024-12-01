spelled_digits = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

# Checks if there are any digits (not including zero) spelled out in 'data' (string)
# returns None if nothing is found
# returns value, index of the first digit found spelled out
# backwards = True will flip data and the digit spelling
def check_spelled_digits(data, backwards=False):
    if backwards: data = data[::-1]

    min_index = float('inf')
    min_value = -1
    spelling_len = 0 # not strictly necessary, but helps us get to the exact index when swapping backwards
    for spelling, value in spelled_digits.items():
        if backwards:
            search = data.find(spelling[::-1])
        else: # backwards == False
            search = data.find(spelling)
        if search > -1 and search < min_index:
            min_index = search
            min_value = value
            spelling_len = len(spelling)

    if min_index != float('inf'):
        if backwards:
            return min_value, len(data) - min_index - (spelling_len)
        else: # backwards == False
            return min_value, min_index
    else: return None

# checks if a digit is in data (string)
# returns None if nothing is found
# returns value, index of first digit found
# backwards = True will flip data and return index as if forward
def check_digits(data, backwards=False):
    if backwards: data = data[::-1]
    for index, char in enumerate(data):
        if char.isdigit():
            if backwards:
                return int(char), len(data) - index - 1
            else: # backwards = False
                return int(char), index
    return None

def main():
    input_file = "day1_input.txt"

    with open(input_file) as f:
        read_data = f.readlines()

        total = 0
        value = 0
        for line in read_data:

            # find spelled out digits (first and last)
            first_spelled = check_spelled_digits(line)
            first_digit = check_digits(line)
            if first_spelled and not first_digit:
                value += first_spelled[0] * 10
            elif first_digit and not first_spelled:
                value += first_digit[0] * 10
            else: # both true
                value += first_spelled[0] * 10 if first_spelled[1] < first_digit[1] else first_digit[0] * 10

            last_spelled = check_spelled_digits(line, backwards=True)
            last_digit = check_digits(line, backwards=True)
            if last_spelled and not last_digit:
                value += last_spelled[0]
            elif last_digit and not last_spelled:
                value += last_digit[0]
            else: # both true
                value += last_spelled[0] if last_spelled[1] > last_digit[1] else last_digit[0]

            total += value
            value = 0

        print(total)
                    

if __name__ == "__main__":
    main()
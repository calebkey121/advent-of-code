def main():
    input_file = "day1_input.txt"

    with open(input_file) as f:
        read_data = f.readlines()

        total = 0
        value = 0
        for line in read_data:
            for char in line:
                if char.isdigit():
                    value += int(char) * 10
                    break
            for char in line[::-1]:
                if char.isdigit():
                    value += int(char)
                    break
            total += value
            value = 0

        print(total)
                    

if __name__ == "__main__":
    main()
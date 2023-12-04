def main():
    input_file = "test.txt"
    scores = {}

    with open(input_file) as f:
        lines = [line.rstrip('\n') for line in f.readlines()]
        
        for line in lines:
            card, numbers = line.split(': ')
            winning_numbers, my_numbers = numbers.split(' | ')
            winning_numbers = winning_numbers.split()
            my_numbers = my_numbers.split()
            
            hits = 0
            for num in my_numbers:
                if num in winning_numbers:
                    hits += 1

            # in format: 'Card number' so split to extract the number
            card = card.split()
            card = int(card[1]) # now card is the number (as a string)

            score = int(hits) # with zero hits, this is 0.5 but truncated will be zero
            scores[card] = score

        print(scores)

        copies = {}

if __name__ == "__main__":
    main()
def main():
    input_file = "day4_input.txt"
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

        copies = {i: 1 for i in range(1,len(scores) + 1)} # each entry is the amount of copies of that card, start with the original

        for card, score in scores.items():
            for _ in range(copies[card]): # run for each copy of the card
                for i in range(card + 1, card + score + 1): # range starts at card + 1 and advances for each hit 
                    if i <= len(copies): # cards will never copy past end of table
                        copies[i] += 1

        total = 0
        for card, copies in copies.items():
            total += copies
        print(total)


if __name__ == "__main__":
    main()
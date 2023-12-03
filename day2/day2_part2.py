def main():
    input_file = "day2_input.txt"
    with open(input_file) as f:
        lines = [line.rstrip('\n') for line in f.readlines()]

        power_sum = 0

        """
        {
            game1: [
                handfull0: {
                    r: 0,
                    g: 4,
                    b: 11
                },
                ...
            ],
            ...
        }
        """
        game_totals = {} # running lists of cubes found during the games

        for line in lines:
            
            game, data = line.split(': ')
            sets = data.split('; ')

            # extract game ids
            game = game.split(' ')
            game_id = int(game[1])

            game_totals[game_id] = []
            color_max = { # track what the highest number pull for each color this game
                'red': 0,
                'green': 0,
                'blue': 0
            }
            # extract game results
            for handfull in sets: # a handfull is one instance of grabbing cubes: "3 red, 8 green, 2 blue" is a handfull
                color_counts = handfull.split(', ') # gives list of 'number color'
                results = {
                    'red': 0,
                    'green': 0,
                    'blue': 0
                }

                for count in color_counts: # count is one color total: "3 red"
                    value, color = count.split(' ')
                    value = int(value)
                    results[color] = value

                    if value > color_max[color]:
                        color_max[color] = value

                game_totals[game_id].append(results)

            power = color_max['red'] * color_max['green'] * color_max['blue']
            print(power)

            power_sum += power

    print(power_sum)



            


            
if __name__ == "__main__":
    main()
import time

def get_surrounding_tiles(x, y, paper_map):
    max_y = len(paper_map) - 1
    max_x = len(paper_map[0]) - 1

    surrounding_tiles = [
        (x - 1, y - 1),
        (x - 1, y),
        (x - 1, y + 1),
        (x, y - 1),
        (x, y + 1),
        (x + 1, y - 1),
        (x + 1, y),
        (x + 1, y + 1),
    ]
    for x, y in surrounding_tiles.copy():
        if x < 0 or x > max_x or y < 0 or y > max_y:
            surrounding_tiles.remove((x, y))
    
    return [paper_map[y][x] for x, y in surrounding_tiles]

def part_1(input_data):
    paper_map = [ row.strip() for row in input_data ]
    
    accessible_papers = 0
    for y, row in enumerate(paper_map):
        for x, tile in enumerate(row):
            if tile == '@':
                # check surrounding 8 tiles
                surrounding_tiles = get_surrounding_tiles(x, y, paper_map)
                papers = surrounding_tiles.count('@')
                if papers < 4:
                    accessible_papers += 1
    return accessible_papers

def find_accessible_papers(paper_map):
    accessible_papers = []
    for y, row in enumerate(paper_map):
        for x, tile in enumerate(row):
            if tile == '@':
                # check surrounding 8 tiles
                surrounding_tiles = get_surrounding_tiles(x, y, paper_map)
                papers = surrounding_tiles.count('@')
                if papers < 4:
                    accessible_papers.append((x, y))
    return accessible_papers

def take_out_papers(paper_map, accessible_papers):
    for x, y in accessible_papers:
        paper_map[y][x] = '.'

def part_2(input_data):
    paper_map = [ list(row.strip()) for row in input_data ]
    
    total_papers = 0
    accessible_papers = find_accessible_papers(paper_map)
    while accessible_papers:
        total_papers += len(accessible_papers)
        take_out_papers(paper_map, accessible_papers)
        accessible_papers = find_accessible_papers(paper_map)
    return total_papers

def main():
    test_input_file = "2025/input/day_4_test_input.txt"
    with open(test_input_file) as f:
        test_input = f.readlines()

    day_input_file = "2025/input/day_4_input.txt"
    with open(day_input_file) as f:
        day_input = f.readlines()
    
    print(f"Test Output Part 1: {part_1(test_input)}")
    print(f"Day Output Part 1: {part_1(day_input)}")
    print(f"Test Output Part 2: {part_2(test_input)}")
    print(f"Day Output Part 2: {part_2(day_input)}")

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    duration = end_time - start_time
    print(f"Time taken: {duration} seconds")

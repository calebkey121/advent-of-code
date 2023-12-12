import time

mapLen = 0
mapData = []

fromSouthPipes = ('|', '7', 'F') # possible pipes to travel to if your are coming from sout
fromNorthPipes = ('|', 'L', 'J')
fromWestPipes = ('-', 'J', '7')
fromEastPipes = ('-', 'L', 'F')

def findNextPipe(loop):
    row = loop[-1][0]
    col = loop[-1][1]
    # Starting from Start
    if len(loop) == 1:
        # if you are coming from a starting position, you have to check all four direction, where there should be two ways
        # Going North (from South)
        if row > 0:
            checkPipes = fromSouthPipes
            direction = (row - 1, col)
            pipe = mapData[direction[0]][direction[1]]
            if (len(loop) == 1  or direction != loop[-2]) and pipe in checkPipes:
                return direction
            
        # Going South (from North)
        if row < mapLen - 1:
            checkPipes = fromNorthPipes
            direction = (row + 1, col)
            pipe = mapData[direction[0]][direction[1]]
            if (len(loop) == 1  or direction != loop[-2]) and pipe in checkPipes:
                return direction

        # Going East (from West) 
        if col < mapLen - 1:
            checkPipes = fromWestPipes
            direction = (row, col + 1)
            pipe = mapData[direction[0]][direction[1]]
            if (len(loop) == 1  or direction != loop[-2]) and pipe in checkPipes:
                return direction

        # Going West (from East)      
        if col > 0:
            checkPipes = fromEastPipes
            direction = (row, col - 1)
            pipe = mapData[direction[0]][direction[1]]
            if (len(loop) == 1  or direction != loop[-2]) and pipe in checkPipes:
                return direction
    else:
        # Just return the direction your letter is pointing
        dx = loop[-2][1] - loop[-1][1]
        dy = loop[-2][0] - loop[-1][0]
        pipe = mapData[row][col]

        north = (row - 1, col)
        south = (row + 1, col)
        east = (row, col + 1)
        west = (row, col - 1)
        if dy == -1:
            # coming from North
            if pipe == '|': return south
            elif pipe == 'J': return west
            elif pipe == 'L': return east
            else: raise RuntimeError("Not a valid pipe")
        elif dy == 1:
            # coming from South
            if pipe == '|': return north
            elif pipe == 'F': return east
            elif pipe == '7': return west
            else: raise RuntimeError("Not a valid pipe")
        elif dx == 1:
            # coming from East
            if pipe == '-': return west
            elif pipe == 'L': return north
            elif pipe == 'F': return south
            else: raise RuntimeError("Not a valid pipe")
        elif dx == -1:
            # coming from West
            if pipe == '-': return east
            elif pipe == 'J': return north
            elif pipe == '7': return south
            else: raise RuntimeError("Not a valid pipe")

    raise RuntimeError("Should have returned something")


    


def main():
    input_file = "day10_input.txt"

    with open(input_file) as f:

        global mapLen, mapData
        mapData = [ line.rstrip('\n') for line in f.readlines() ]
        mapLen = len(mapData)

        loop = []
        
        start = None
        for row in range(mapLen):
            for col in range(mapLen):
                if mapData[row][col] == 'S':
                    start = (row, col)
                    loop.append(start)
                    break
            if start: break
            
        nextPipe = findNextPipe(loop)
        loop.append(nextPipe)

        while loop[-1] != start:
            nextPipe = findNextPipe(loop)
            loop.append(nextPipe)

        print(len(loop) // 2)


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    duration = end_time - start_time
    print(f"Time taken: {duration} seconds")
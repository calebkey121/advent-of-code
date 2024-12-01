import time

mapWidth = 0
mapHeight = 0
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
        if row < mapHeight - 1:
            checkPipes = fromNorthPipes
            direction = (row + 1, col)
            pipe = mapData[direction[0]][direction[1]]
            if (len(loop) == 1  or direction != loop[-2]) and pipe in checkPipes:
                return direction

        # Going East (from West) 
        if col < mapWidth - 1:
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


def replaceStart(loop):
    start = loop[0]
    before = loop[1]
    after = loop[-2]

    direction = []

    dx1 = start[1] - before[1]
    dy1 = start[0] - before[0]
    dx2 = start[1] - after[1]
    dy2 = start[0] - after[0]

    if dx1 == 1 or dx2 == 1:
        direction.append('west')
    if dx1 == -1 or dx2 == -1:
        direction.append('east')
    if dy1 == 1 or dy2 == 1:
        direction.append('north')
    if dy1 == -1 or dy2 == -1:
        direction.append('south')
    
    if 'north' in direction and 'south' in direction:
        return '|'
    elif 'east' in direction and 'west' in direction:
        return '-'
    elif 'south' in direction and 'west' in direction:
        return '7'
    elif 'south' in direction and 'east' in direction:
        return 'F'
    elif 'north' in direction and 'west' in direction:
        return 'J'
    elif 'north' in direction and 'east' in direction:
        return 'L'
    else:
        raise RuntimeError("replaceStart failed to find the proper pipe")



def main():
    input_file = "day10_input.txt"

    with open(input_file) as f:

        global mapWidth, mapHeight, mapData
        mapData = [ line.rstrip('\n') for line in f.readlines() ]
        mapHeight = len(mapData)
        mapWidth = len(mapData[0])

        loop = []
        
        start = None
        for row in range(mapHeight):
            for col in range(mapWidth):
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

        mapData[row] = mapData[row][:col] + replaceStart(loop) + mapData[row][col + 1:]
        

        revisedMap = []
        total = 0
        for row in range(mapHeight):
            revisedString = ""
            outside = True
            potentialBreak = None
            for col in range(mapWidth):
                if (row, col) in loop:
                    pipe = mapData[row][col]
                    if pipe == '|': 
                        outside = not outside

                    if not potentialBreak:
                        if pipe in ('L', 'F'):
                            potentialBreak = pipe
                    else:
                        if (potentialBreak == 'L' and pipe == '7') or (potentialBreak == 'F' and pipe == 'J'):
                            potentialBreak = None
                            outside = not outside
                        elif pipe == '-':
                            pass
                        else:
                            potentialBreak = None
                    

                    revisedString += pipe
                else:
                    potentialBreak = None
                    if outside:
                        revisedString += 'O'
                    else: 
                        revisedString += 'I'
                        total += 1
            revisedMap.append(revisedString)

        print(len(loop) // 2)
        print(total)
                

                



if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    duration = end_time - start_time
    print(f"Time taken: {duration} seconds")
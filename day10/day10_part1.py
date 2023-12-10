import time

pipeLen = 0

class Pipe():
    def __init__(self, pipeType, row, col, visited=False) -> None:
        self.pipeType = pipeType
        self.row = row
        self.col = col
        self.visited = visited
        self.north = self.south = self.east = self.west = None

        if self.row > 0:
            self.north = (self.row - 1, self.col)
        if self.row < pipeLen - 1:
            self.south = (self.row + 1, self.col)
        if self.col > 0:
            self.east = (self.row, self.col - 1)
        if self.col < pipeLen - 1:
            self.west = (self.row, self.col + 1)

    def __repr__(self) -> str:
        return self.pipeType
    

def findNextPipe(pipeMap, pipe):
    northPipes = ('|', '7', 'F', 'S') # more like 'from south pipes' but lets simplify to if youre going north pipes
    if pipe.north:
        path = pipeMap[pipe.north[0]][pipe.north[1]]
        if not path.visited and path.pipeType in northPipes:
            path.visited = True
            return path
        
    southPipes = ('|', 'L', 'J', 'S')
    if pipe.south:
        path = pipeMap[pipe.south[0]][pipe.south[1]]
        if not path.visited and path.pipeType in southPipes:
            path.visited = True
            return path
        
    eastPipes = ('-', 'L', 'F', 'S')
    if pipe.east:
        path = pipeMap[pipe.east[0]][pipe.east[1]]
        if not path.visited and path.pipeType in eastPipes:
            path.visited = True
            return path
        
    westPipes = ('-', 'J', '7', 'S')
    if pipe.west:
        path = pipeMap[pipe.west[0]][pipe.west[1]]
        if not path.visited and path.pipeType in westPipes:
            path.visited = True
            return path
        
    raise RuntimeError("Should never not find one")


    


def main():
    input_file = "day10_input.txt"

    with open(input_file) as f:

        mapData = [ line.rstrip('\n') for line in f.readlines() ]
        pipeMap = []

        loop = []
        global pipeLen 
        pipeLen = len(mapData)
        
        for row in range(len(mapData)):
            pipeMap.append([])
            for col in range(len(mapData[row])):
                if mapData[row][col] == 'S':
                    start = (Pipe('S', row, col, visited=True))
                    loop.append(start)
                    pipeMap[row].append(start)
                else:
                    pipeMap[row].append(Pipe(mapData[row][col], row, col))

        # Start finding the mainloop
        nextPipe = findNextPipe(pipeMap, loop[-1])
        loop.append(nextPipe)
        nextPipe = findNextPipe(pipeMap, loop[-1])
        loop.append(nextPipe)
        start.visited = False
        while loop[-1] != start:
            nextPipe = findNextPipe(pipeMap, loop[-1])
            loop.append(nextPipe)
            
        print(len(loop) // 2)


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    duration = end_time - start_time
    print(f"Time taken: {duration} seconds")
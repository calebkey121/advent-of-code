import time
from math import lcm

# 3863263 too low
# 41190697 too low
# 159219880 too low
# 280868675 wont tell me
# 1243836193 wont tell me
# 2052853129
# 2613314269 i give, apparently its 14 digits
# 23977527174353

class Node():
    def __init__(self, id, left, right) -> None:
        self.id = id
        self.left = left
        self.right = right
        
    def __repr__(self) -> str:
        return self.id

def main():
    input_file = "day8_input.txt"

    with open(input_file) as f:
        lines = [ line.rstrip(")\n") for line in f.readlines() ]

        instructions = lines[0]
        nodes = []
        for line in lines[2:]:
            nodeID = line.split(" = ")[0]
            left, right = line.split(" = (")[1].split(", ")
            nodes.append(Node(id=nodeID, left=left, right=right))

        for node in nodes:
            target = node.left
            for l in nodes:
                if l.id == target:
                    node.left = l
                    break
            target = node.right
            for r in nodes:
                if r.id == target:
                    node.right = r
                    break

        # Find all starting nodes
        zSteps = [] # will store the number of steps to take to z
        for node in nodes:
            if node.id[-1] == 'A':
                # Found a node that ends in A, get to the z and record the num of steps
                found = False
                steps = 0
                while not found:
                    for direction in instructions:
                        if node.id[-1] == 'Z':
                            found = True
                            zSteps.append(steps)
                            break
                        if direction == 'R':
                            node = node.right
                        elif direction == 'L':
                            node = node.left
                        steps += 1

        print(lcm(*zSteps))


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    duration = end_time - start_time
    print(f"Time taken: {duration} seconds")
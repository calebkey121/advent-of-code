import time

# 3863263 too low
# 41190697 too low
# 159219880 too low
# 280868675 wont tell me
# 1243836193 wont tell me
# 2052853129
# 2613314269 i give, apparently its 14 digits

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

        curr = []
        # Find all starting nodes
        for node in nodes:
            if node.id[-1] == "A":
                curr.append(node)


        found = False
        steps = 0
        while not found:
            for direction in instructions:
                # see if all found the end
                for node in curr:
                    found = True
                    if node.id[-1] != 'Z':
                        found = False
                        break # continue on below
                if found: break # if you get out of the above loop, break
                if direction == 'L': # left
                    for node in range(len(curr)):
                        curr[node] = curr[node].left
                elif direction == 'R': # right
                    for node in range(len(curr)):
                        curr[node] = curr[node].right
                steps += 1

        print(steps)


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    duration = end_time - start_time
    print(f"Time taken: {duration} seconds")
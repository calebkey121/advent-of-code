import time

# 108100679 too high

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

        for node in nodes:
            if node.id == "AAA":
                curr = node


        found = False
        steps = 0
        while not found:
            for direction in instructions:
                if curr.id == "ZZZ": # Found the end
                    found = True
                    break
                if steps > 108100679: # for debugging
                    raise ValueError("Went past max steps")
                if curr == curr.left == curr.right:
                    raise RuntimeError("Infinite Loop")
                if direction == 'L': # left
                    curr = curr.left
                elif direction == 'R': # right
                    curr = curr.right
                steps += 1

        print(steps)


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    duration = end_time - start_time
    print(f"Time taken: {duration} seconds")
import time

class Node:
    def __init__(self, source):
        self._source = source
        self._dest = None
        self._parents = []
        self._can_reach_dac = False
        self._can_reach_fft = False
        self._can_reach_out = False
    
    def set_dest(self, dest):
        self._dest = dest
    
    def __repr__(self):
        return f"{self._source}"

def search_out_p1(node, visited=set()):
    if node._source == 'out':
        return 1
    #visited.add(node._source)
    found = 0
    for d in node._dest:
        found += search_out_p1(d, visited)
    return found

def part_1(input_data):
    graph = {}
    for line in input_data:
        source, rest = line.rstrip().split(":")
        dest = rest.split()
        graph[source] = dest
    
    nodes = {source: Node(source) for source in graph}
    nodes['out'] = Node("out")
    for source, dest in graph.items():
        nodes[source].set_dest([nodes[d] for d in dest])
    root = nodes['you']
    return search_out_p1(root)


def part_2(input_data):
    graph = {}
    for line in input_data:
        source, rest = line.rstrip().split(":")
        dest = rest.split()
        graph[source] = dest
    
    nodes = {source: Node(source) for source in graph}
    nodes['out'] = Node("out")
    for source, dest in graph.items():
        nodes[source].set_dest([nodes[d] for d in dest])
        for d in dest:
            nodes[d]._parents.append(nodes[source])
    
    def set_parents_fft(node):
        if node._source == 'svr':
            return
        for p in node._parents:
            if p._can_reach_fft:
                continue
            p._can_reach_fft = True
            set_parents_fft(p)
    
    def set_parents_dac(node):
        if node._source == 'svr':
            return
        for p in node._parents:
            if p._can_reach_dac:
                continue
            p._can_reach_dac = True
            set_parents_dac(p)

    def set_parents_out(node):
        if node._source == 'svr':
            return
        for p in node._parents:
            if p._can_reach_out:
                continue
            p._can_reach_out = True
            set_parents_out(p)

    set_parents_out(nodes['out'])
    set_parents_dac(nodes['dac'])
    set_parents_fft(nodes['fft'])

    root = nodes['svr']
    return search_out_p2(root, {})

def search_out_p2(node, cache, dac=False, fft=False):
    if node._source == 'out' and all([dac, fft]):
        return 1
    elif not node._can_reach_out:
        return 0
    if node._source == 'dac':
        dac = True
    elif node._source == 'fft':
        fft = True
    if (node._source, dac, fft) in cache:
        return cache[(node._source, dac, fft)]
    can_reach = [node._can_reach_dac, node._can_reach_fft]
    for i, reached in enumerate([dac, fft]):
        if not reached and not can_reach[i]:
            return 0
        
    found = 0
    for d in node._dest:
        found += search_out_p2(d, cache, dac, fft)
    cache[(node._source, dac, fft)] = found
    return found

def main():
    test_input_file = "2025/input/day_11_test_input.txt"
    with open(test_input_file) as f:
        test_input = f.readlines()
    
    test_input_file_p2 = "2025/input/day_11_test_input_p2.txt"
    with open(test_input_file_p2) as f:
        test_input_p2 = f.readlines()

    day_input_file = "2025/input/day_11_input.txt"
    with open(day_input_file) as f:
        day_input = f.readlines()
    
    print(f"Test Output Part 1: {part_1(test_input)}")
    print(f"Day Output Part 1: {part_1(day_input)}")
    print(f"Test Output Part 2: {part_2(test_input_p2)}")
    print(f"Day Output Part 2: {part_2(day_input)}")

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    duration = end_time - start_time
    print(f"Time taken: {duration} seconds")

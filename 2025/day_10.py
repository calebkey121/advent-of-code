import time
from ast import literal_eval
import sympy as sp
import pulp

def compositions(total, k, max_presses=None):
    # If no max_presses provided, treat as unlimited
    if max_presses is None:
        max_presses = [None] * k

    if k == 1:
        last = total
        # Check the last element against max limit
        if max_presses[-1] is None or last <= max_presses[-1]:
            yield (last,)
        return

    for i in range(total + 1):
        # Check limit for this position
        limit = max_presses[0]
        if limit is not None and i > limit:
            continue

        # Recurse with remaining slots and remaining maxes
        for rest in compositions(total - i, k - 1, max_presses[1:]):
            yield (i,) + rest

def parse_machines(input_data):
    machines = []
    for line in input_data:
        split = line.rstrip().split(' ')
        lights = []
        for light in split[0][1:-1]:
            if light == '#':
                lights.append(1)
            else:
                lights.append(0)
        buttons = []
        for button in split[1:-1]:
            buttons.append([int(a) for a in button[1:-1].split(',')])
        joltage = literal_eval(f"[{split[-1][1:-1]}]")
        machines.append([lights, buttons, joltage])
    return machines

def min_light_presses(lights, buttons):
    # loop until you find the combination
    i = 1
    while True:
        for combo in compositions(i, len(buttons)):
            curr = [0] * len(lights)
            for button_idx, presses in enumerate(combo):
                if presses:
                    button = buttons[button_idx]
                    for light in button:
                        curr[light] += presses
            if lights == [a % 2 for a in curr]:
                return sum(combo)
        i += 1

def part_1(input_data):
    machines = parse_machines(input_data)
    total = 0
    for lights, buttons, joltage in machines:
        total += min_light_presses(lights, buttons)
    return total

def min_joltage_presses(joltages, buttons):
    i = max(joltages)
    
    A = [
        ([0] * len(buttons)) for _ in range(len(joltages))
    ]
    for i, button in enumerate(buttons):
        for light in button:
            A[light][i] = 1
    b = joltages
    # ILP
    prob = pulp.LpProblem("min_solution", pulp.LpMinimize)

    # integer decision variables >= 0
    x = [pulp.LpVariable(f"x{i}", lowBound=0, cat="Integer") for i in range(len(A[0]))]

    # constraints A*x = b
    for r in range(len(A)):
        prob += pulp.lpSum(A[r][c] * x[c] for c in range(len(A[0]))) == b[r]

    # objective: minimize sum(x)
    prob += pulp.lpSum(x)

    # solve
    prob.solve(pulp.PULP_CBC_CMD(msg=False))
    solution = [v.value() for v in x]
    return int(sum(solution))
    

def part_2(input_data):
    machines = parse_machines(input_data)
    total = 0
    for i, (lights, buttons, joltages) in enumerate(machines):
        #print(f"{i + 1} / {len(machines)}")
        total += min_joltage_presses(joltages, buttons)
    return total
# too low 12823

def main():
    test_input_file = "2025/input/day_10_test_input.txt"
    with open(test_input_file) as f:
        test_input = f.readlines()

    day_input_file = "2025/input/day_10_input.txt"
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

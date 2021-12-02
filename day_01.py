# Day 1 - Part 1

# Reading in the file
with open('inputs/01_01.txt') as f:
    puzzle_input = [int(line.strip()) for line in f]

def part_one(inputs):
    count = 0

    previous = inputs[0]
    for i in range(1, len(inputs)):
        current = inputs[i]
        if current > previous:
            count += 1
        previous = current
    
    return count

# part_one(puzzle_input)

# Day 1 - Part 2

def part_two(inputs):
    new_list = []
    for i in range (0, len(inputs)-2):
        addition = inputs[i] + inputs[i+1] + inputs[i+2]
        new_list.append(addition)
    
    return part_one(new_list)


part_two(puzzle_input)

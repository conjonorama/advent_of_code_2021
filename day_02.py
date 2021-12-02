# Day 2 - Part 1

with open('inputs/02_01.txt', 'r') as f:
    puzzle_input = [line.strip() for line in f]

def coordinates(input):
    horizontal_pos = 0
    vertical_pos = 0

    for i in input:
        dir = i.split()[0]
        mag = i.split()[1]
        if dir == "forward":
            horizontal_pos += int(mag)
        if dir == "up":
            vertical_pos -= int(mag)
        elif dir == "down":
            vertical_pos += int(mag)
    
    return horizontal_pos*vertical_pos

coordinates(puzzle_input)

# Day 2 - Part Two

def coordinates_two(input):
    horiz_pos = 0
    vert_pos = 0
    aim = 0

    for i in input:
        dir = i.split()[0]
        mag = int(i.split()[1])
        if dir == 'forward':
            horiz_pos += mag
            vert_pos += (mag * aim)
        if dir == 'up':
            aim -= mag
        if dir == 'down':
            aim += mag
    
    return horiz_pos*vert_pos

coordinates_two(puzzle_input)




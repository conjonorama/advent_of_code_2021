# Day 5 - Hydrothermal Vents - Part 1
from collections import Counter

with open('inputs/05_01.txt', 'r') as f:
    puzzle_input = [line.strip() for line in f]


d = Counter()

for line in puzzle_input:
    p0, p1 = line.split(' -> ')
    p0 = [int(x) for x in p0.split(',')]
    p1 = [int(x) for x in p1.split(',')]
    
    # if p0[0] != p1[0] and p0[1] != p1[1]:
    #     continue

    dx = p1[0] - p0[0]
    dy = p1[1] - p0[1]

    if dx > 0:
        dx = 1
    elif dx < 0:
        dx = -1
    else:
        dx = 0
    
    if dy > 0:
        dy = 1
    elif dy < 0:
        dy = -1
    else:
        dy = 0

    # print(p0, p1)
    x, y = p0
    while (x, y) != tuple(p1):
        d[(x, y)] += 1
        x += dx
        y += dy
        # print(x, y)
    d[tuple(p1)] += 1

ans = sum(v >= 2 for k, v in d.items())

print(ans)

  


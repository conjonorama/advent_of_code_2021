# Day 09 - Smoke Basin

# Find low points

with open('inputs/09_01.txt', 'r') as f:
    puzzle_input = [line.strip() for line in f.readlines()]

print(puzzle_input[:4])

test_data = '''
2199943210
3987894921
9856789892
8767896789
9899965678
'''
print(test_data.strip().split('\n'))

def low_points(inp):
    line_len = len(inp[0])
    for i in range(0, len(inp)-1):
        print(inp[i])

low_points(test_data.strip().split('\n'))
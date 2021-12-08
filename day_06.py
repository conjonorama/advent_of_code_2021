# Puzzle input

with open('inputs/06_01.txt', 'r') as f:
    puzzle_input = []
    for i in f.read().strip().split(','):
        puzzle_input.append(int(i))

print(puzzle_input)

fish = [puzzle_input.count(i) for i in range(9)]

for i in range(256):
    num = fish.pop(0)
    fish[6] += num
    fish.append(num)
    assert len(fish) == 9
print(sum(fish))






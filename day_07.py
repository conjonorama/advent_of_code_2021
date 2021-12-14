# Day 7

with open('inputs/07_01.txt', 'r') as f:
    puzzle_input = [int(n) for n in f.read().strip().split(',')]

# Part One

def dist(f_input):
    max_t, min_t = max(f_input), min(f_input)
    d = {n: 0 for n in range(min_t, max_t + 1)}
    for k, v in d.items():
        for i in f_input:
            d[k] = d.get(k, 0) + abs(i-k)
    return min(d.values())

dist(puzzle_input)

# Part Two

def dist_2(f_input):
    max_t, min_t = max(f_input), min(f_input)
    d = {n: 0 for n in range(min_t, max_t + 1)}
    for k, v in d.items():
        for i in f_input:
            d[k] = d.get(k, 0) + ari_seq(abs(i - k), 1)
    
    return min(d.values())

def ari_seq(n, a, d = 1):
    return n/2 * (2*a + (n-1) * d)

print(dist_2(puzzle_input))
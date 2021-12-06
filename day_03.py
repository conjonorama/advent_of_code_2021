from collections import Counter

with open("inputs/03_01.txt") as f:
    puzzle_input = [line.strip() for line in f]

def gamma_rate(input):
    t = [0] * len(input[0])
    for i in input:
        for k, j in enumerate(i):
            t[k] += int(j)

    t2 = []        
    for i in t:
        t2.append(str(round(i / len(input))))
        
       
    return t2

gamma_rate(puzzle_input)

def epsilon_rate(input):
    g_rate = gamma_rate(input)

    t = []
    for i in g_rate:
        if i == '0':
            t.append('1')
        else:
            t.append('0')
    return t

epsilon_rate(puzzle_input)

def binary_converter(input):

    return int(''.join(input), 2)

binary_converter(gamma_rate(puzzle_input)) * binary_converter(epsilon_rate(puzzle_input))

# def oxygen_generator(input):
#     g_rate = gamma_rate(input)

#     new_list = []

#     for i in 

# Stolen from Reddit - will come back and re-attempt 
def rating(data, cmp):
    for i in range(len(data[0])):
        _01 = {"0": [], "1": []}

        for number in data:
            _01[number[i]].append(number)

        if len(data := _01[
            "1" if cmp(len(_01["1"]), len(_01["0"])) else "0"
           ]) == 1:
            return int(data[0], 2)


print(rating(puzzle_input[:], int.__ge__) * rating(puzzle_input[:], int.__lt__))

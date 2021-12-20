# Day 8

with open('inputs/08_01.txt', 'r') as f:
    puzzle_input = [line.strip() for line in f.readlines()]

# Part One

# Sample Data
t = '''be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce'''.split('\n')

def instances(inp):
    count = 0
    for line in inp:
        output_vals = line.split('|')[1]
        for i in output_vals.split():          
            if len(i) == 2 or len(i) == 3 or len(i) == 4 or len(i) == 7:
                count += 1
            

    
    return count

# print(instances(puzzle_input))

# Part Two - stolen from Reddit

def instances_two(inp):
    sum_of_n = 0
    for line in inp:
        wires, output = line.split(' | ')
        wires = wires.split()
        output = output.split()

        displays = {0: '', 1:'', 2:'', 3:'', 4:'', 5:'', 6:'', 7:'', 8:'', 9:''}

        left_triple = []
        right_triple = []

        for w in wires:
            l = len(w)
            if l == 2: displays[1] = set(w)
            if l == 3: displays[7] = set(w)
            if l == 4: displays[4] = set(w)
            if l == 5: left_triple.append(set(w))
            if l == 6: right_triple.append(set(w))
            if l == 7: displays[8] = set(w)

        for w in right_triple:
            if displays[4].issubset(set(w)):
                displays[9] = set(w)
            else:
                if displays[7].issubset(set(w)):
                    displays[0] = set(w)
                else:
                    displays[6] = set(w)

        for w in left_triple:
            if displays[7].issubset(set(w)):
                displays[3] = set(w)
            else:
                if len(set(w).intersection(displays[4])) == 3:
                    displays[5] = set(w)
                else:
                    displays[2] = set(w)
            
        digits = ''
        for n in output:
            s = set(n)
            for i, key in enumerate(displays.values()):
                if s == key:
                    digits = digits + str(i)
        sum_of_n += int(digits)
    
    return(sum_of_n)

instances_two(puzzle_input)



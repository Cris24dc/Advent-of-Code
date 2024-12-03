import re

def elem_mul(elem):
    return int((elem.split(',')[0]).split('(')[1]) * int((elem.split(',')[1]).split(')')[0])\

with open("day3.txt", "r") as f:
    result = 0
    compute = True

    match = re.findall(r'mul\([0-9]*,[0-9]*\)|do\(\)|don\'t\(\)', f.read().strip())

    for elem in match:
        if elem == "do()":
            compute = True
        elif elem == "don't()":
            compute = False
        else:
            if compute:
                result += elem_mul(elem)

    print(result)

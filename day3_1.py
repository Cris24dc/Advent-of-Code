import re

with open("day3.txt", "r") as f:
    result = 0
    for x, y in re.findall(r'mul\((\d+),(\d+)\)', f.read().strip()):
        result += int(x) * int(y)
    print(result)

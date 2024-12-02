list1 = []
list2 = []
distance = 0

with open("day1.txt", "r") as f:
    for line in f:
        line_splited = line.split()
        list1.append(int(line_splited[0]))
        list2.append(int(line_splited[1]))

list1.sort()
list2.sort()

for elem1, elem2 in zip(list1, list2):
    distance = distance + abs(elem1-elem2)

print(distance)
    
list1 = []
list2 = []
distance = 0

with open("day1.txt", "r") as f:
    for line in f:
        line_splited = line.split()
        list1.append(int(line_splited[0]))
        list2.append(int(line_splited[1]))

for elem1 in list1:
    distance = distance + elem1 * list2.count(elem1)

print(distance)
    
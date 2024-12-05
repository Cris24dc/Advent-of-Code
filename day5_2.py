def read():
    order = []
    update = []
    with open("day5.txt", "r") as f:
        for line in f:
            line = line.strip()
            if '|' in line:
                order.append(tuple(map(int, line.split('|'))))
            elif ',' in line:
                update.append(list(map(int, line.split(','))))
    return (order, update)

order, update = read()
sum = 0

for arr in update:
    ok = 1
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if(tuple([arr[i], arr[j]]) not in order):
                ok = 0
                arr[i], arr[j] = arr[j], arr[i]

    if ok == 0:
        sum += arr[len(arr)//2]

print(sum)
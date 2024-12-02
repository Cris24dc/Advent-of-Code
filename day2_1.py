def asc_desc(rep):
    for i in range(1, len(rep)):
        diff = rep[i] - rep[i - 1]
        if not (rep[i] > rep[i - 1]) or not (1 <= diff <= 3):
            return False
    return True

def safe(rep):
    return asc_desc(rep) or asc_desc(rep[::-1])

def result():
    safe_nr = 0
    with open("day2.txt", "r") as f:
        for line in f:
            line_splited = list(map(int, (line.split())))
            if safe(line_splited):
                safe_nr = safe_nr + 1
    return safe_nr

print(result())

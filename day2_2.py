def is_safe(rep):
    for i in range(1, len(rep)):
        diff = rep[i] - rep[i - 1]
        if not (1 <= abs(diff) <= 3):
            return False
    return rep == sorted(rep) or rep == sorted(rep, reverse=True)

def can_be_safe(rep):
    for i in range(len(rep)):
        new_rep = rep[:i] + rep[i + 1:]
        if is_safe(new_rep):
            return True
    return False

def safe(rep):
    return is_safe(rep) or can_be_safe(rep)

def result():
    safe_count = 0
    with open("day2.txt", "r") as f:
        for line in f:
            levels = list(map(int, line.split()))
            if safe(levels):
                safe_count += 1
    return safe_count

print(result())
def read_matrix():
    matrix = []
    with open("day4.txt", "r") as f:
        for line in f:
            line = line.strip()
            matrix.append(list(line))
    return matrix

def get_rows(matrix):
    return ["".join(row) for row in matrix]

def get_columns(matrix):
    n = len(matrix)
    m = len(matrix[0]) if n > 0 else 0
    return ["".join(matrix[i][j] for i in range(n)) for j in range(m)]

def get_main_diagonals(matrix):
    n = len(matrix)
    diagonals = []
    for k in range(-n + 1, n):
        diag = ""
        for i in range(n):
            j = i + k
            if 0 <= i < n and 0 <= j < len(matrix[i]):
                diag += matrix[i][j]
        if diag:
            diagonals.append(diag)
    return diagonals

def get_leading_diagonals(matrix):
    n = len(matrix)
    m = len(matrix[0]) if n > 0 else 0
    diagonals = []
    for k in range(n + m - 1):
        diag = ""
        for i in range(n):
            j = k - i
            if 0 <= i < n and 0 <= j < m:
                diag += matrix[i][j]
        if diag:
            diagonals.append(diag)
    return diagonals

def main():
    matrix = read_matrix()
    nr = 0

    for elem in get_rows(matrix):
        nr += elem.count("XMAS")
        nr += elem.count("SAMX")
    for elem in get_columns(matrix):
        nr += elem.count("XMAS")
        nr += elem.count("SAMX")
    for elem in get_main_diagonals(matrix):
        nr += elem.count("XMAS")
        nr += elem.count("SAMX")
    for elem in get_leading_diagonals(matrix):
        nr += elem.count("XMAS")
        nr += elem.count("SAMX")

    print(nr)

if __name__ == "__main__":
    main()
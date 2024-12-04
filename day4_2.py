def read_matrix(file_name="day4.txt"):
    with open(file_name, "r") as f:
        return [list(line.strip()) for line in f]

def is_mas(matrix, i, j):
    patterns = [
        [('M', 'S'), ('A',), ('M', 'S')],
        [('S', 'S'), ('A',), ('M', 'M')],
        [('S', 'M'), ('A',), ('S', 'M')],
        [('M', 'M'), ('A',), ('S', 'S')],
    ]
    
    return any(
        matrix[i][j] == p[0][0] and matrix[i][j + 2] == p[0][1] and
        matrix[i + 1][j + 1] == p[1][0] and
        matrix[i + 2][j] == p[2][0] and matrix[i + 2][j + 2] == p[2][1]
        for p in patterns
    )

def main():
    matrix = read_matrix()
    nr = sum(
        is_mas(matrix, i, j)
        for i in range(len(matrix) - 2)
        for j in range(len(matrix[i]) - 2)
    )
    print(nr)

if __name__ == "__main__":
    main()

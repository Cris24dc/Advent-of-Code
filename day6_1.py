def read_map(file_name):
    map_data = []
    with open(file_name, "r") as f:
        for line in f:
            map_data.append([x for x in line if x != '\n'])
    return map_data

def player_position(map_data):
    for i in range(len(map_data)):
        for j in range(len(map_data[i])):
            if map_data[i][j] in "^><v":
                return i, j
    raise ValueError("Player doesn't exist on the map.")

def get_dir_symbol(direction):
    symbols = {"up": "^", "right": ">", "down": "v", "left": "<"}
    return symbols.get(direction, None)

def change_dir(direction):
    directions = ["up", "right", "down", "left"]
    if direction not in directions:
        raise ValueError("Invalid direction.")
    return directions[(directions.index(direction) + 1) % len(directions)]

def move_player(map_data, pos, direction):
    deltas = {"up": (-1, 0), "right": (0, 1), "down": (1, 0), "left": (0, -1)}
    delta = deltas[direction]
    new_pos = (pos[0] + delta[0], pos[1] + delta[1])

    if not on_map(new_pos, map_data):
        map_data[pos[0]][pos[1]] = 'X'
        return map_data, None, None

    if map_data[new_pos[0]][new_pos[1]] != '#':
        map_data[pos[0]][pos[1]] = 'X'
        map_data[new_pos[0]][new_pos[1]] = get_dir_symbol(direction)
        return map_data, new_pos, direction
    
    else:
        direction = change_dir(direction)
        map_data[pos[0]][pos[1]] = get_dir_symbol(direction)
        return map_data, pos, direction

def on_map(pos, map_data):
    return 0 <= pos[0] < len(map_data) and 0 <= pos[1] < len(map_data[0])

def print_map(map_data):
    for row in map_data:
        print(" ".join(row))
    print()

def main():
    map_data = read_map("day6.txt")
    direction = "up"
    pos = player_position(map_data)

    while pos:
        map_data, pos, direction = move_player(map_data, pos, direction)

    path = lambda map_data: sum(row.count('X') for row in map_data)
    print(path(map_data))

if __name__ == "__main__":
    main()

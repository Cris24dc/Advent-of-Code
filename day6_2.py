def read_map(file_name):
    map_data = []
    with open(file_name, "r") as f:
        for line in f:
            map_data.append([x for x in line.strip()])
    return map_data

def copy_map(a_map):
    return [row[:] for row in a_map]

def find_path_steps(map_data, start):
    x, y = start
    path_map = {}

    dir_x, dir_y = 0, -1

    path_map[(x, y)] = {"c": 1, "dx": dir_x, "dy": dir_y}

    while True:
        next_x = x + dir_x
        next_y = y + dir_y

        if next_x < 0 or next_x >= len(map_data[0]) or next_y < 0 or next_y >= len(map_data):
            break

        if map_data[next_y][next_x] == "#":
            if dir_y == -1:
                dir_x, dir_y = 1, 0
            elif dir_y == 1:
                dir_x, dir_y = -1, 0
            elif dir_x == -1:
                dir_x, dir_y = 0, -1
            else:
                dir_x, dir_y = 0, 1
        else:
            x, y = next_x, next_y
            key = (x, y)

            if key in path_map:
                prev_state = path_map[key]
                if prev_state["dx"] == dir_x and prev_state["dy"] == dir_y:
                    return {"loop": True, "size": len(path_map)}

            path_map[key] = {"c": path_map.get(key, {"c": 0})["c"] + 1, "dx": dir_x, "dy": dir_y}

    return {"loop": False, "size": len(path_map)}

def find_loop_count(map_data, start):
    loop_count = 0

    for i in range(len(map_data)):
        for j in range(len(map_data[i])):
            if (i, j) == start:
                continue

            new_map = copy_map(map_data)
            new_map[i][j] = "#"

            result = find_path_steps(new_map, start)
            if result["loop"]:
                loop_count += 1

    return loop_count

def main():
    map_data = read_map("day6.txt")
    start = None

    for y in range(len(map_data)):
        for x in range(len(map_data[y])):
            if map_data[y][x] == "^":
                start = (x, y)
                map_data[y][x] = "."
                break

    if not start:
        print("Eroare: Nu există jucător pe hartă.")
        return

    path_steps = find_path_steps(map_data, start)
    loop_count = find_loop_count(map_data, start)

    print(f"Dimensiunea traseului: {path_steps['size']}")
    print(f"Numărul de cicluri: {loop_count}")

if __name__ == "__main__":
    main()

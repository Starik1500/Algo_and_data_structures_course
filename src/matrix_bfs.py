import os
from collections import deque

ROW = 11
COL = 10

row_num = [-1, 0, 0, 1]
col_num = [0, -1, 1, 0]


def create_coordinate(x: int, y: int):
    return (x, y)


def create_queue_node(corcell, dist: int):
    return (corcell, dist)


def is_valid(row: int, col: int):
    return 0 <= row < ROW and 0 <= col < COL


def bfs(mat, src, dest):
    if mat[src[0]][src[1]] != 1 or mat[dest[0]][dest[1]] != 1:
        return -1

    visited = [[False for n in range(COL)] for n in range(ROW)]
    visited[src[0]][src[1]] = True
    queue = deque()
    source = create_queue_node(src, 0)
    queue.append(source)

    while queue:
        current = queue.popleft()
        cordinate_cell = current[0]
        if cordinate_cell == dest:
            return current[1]

        for i in range(4):
            row = cordinate_cell[0] + row_num[i]
            col = cordinate_cell[1] + col_num[i]

            if is_valid(row, col) and mat[row][col] == 1 and not visited[row][col]:
                visited[row][col] = True
                neighbor_cell = create_queue_node((row, col), current[1] + 1)
                queue.append(neighbor_cell)
    return -1


def main():
    input_file_path = os.path.join(os.path.dirname(__file__), 'matrix_input.txt')
    output_file_path = os.path.join(os.path.dirname(__file__), 'matrix_output.txt')

    with open(input_file_path, "r") as file:
        start_point = list(map(int, file.readline().split(", ")))
        end_point = list(map(int, file.readline().split(", ")))
        ROW, COL = map(int, file.readline().split(","))
        mat = []
        for n in range(ROW):
            row = list(map(int, file.readline().strip()[1:-1].split()))
            mat.append(row)

    source = create_coordinate(start_point[0], start_point[1])
    dest = create_coordinate(end_point[0], end_point[1])
    dist = bfs(mat, source, dest)

    with open(output_file_path, "w") as file:
        file.write(str(dist))


if __name__ == "__main__":
    main()

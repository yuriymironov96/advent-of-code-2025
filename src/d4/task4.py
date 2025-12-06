from copy import deepcopy

Matrix = list[list[bool]]


FILLED_NEIGHBOURS_ALLOWED = 4


def read_input() -> Matrix:
    matrix = []
    for row in open("input.txt", "r"):
        matrix.append(
            [True if char == "@" else False for char in row.replace("\n", "")]
        )
    return matrix


def is_approachable(matrix: Matrix, x: int, y: int) -> bool:
    filled_neighbours = 0

    if not matrix[y][x]:
        return False

    for neighbour_y in range(y - 1, y + 2):
        for neighbour_x in range(x - 1, x + 2):
            try:
                if neighbour_x == x and neighbour_y == y:
                    continue
                if neighbour_x not in range(0, len(matrix[0])):
                    continue
                if neighbour_y not in range(0, len(matrix)):
                    continue
                if matrix[neighbour_y][neighbour_x]:
                    filled_neighbours += 1
            except IndexError:
                continue
    return filled_neighbours < FILLED_NEIGHBOURS_ALLOWED


def task_one():
    print("parsing input...")
    matrix = read_input()
    print("input parsed")

    approachable_count = 0

    for y, row in enumerate(matrix):
        print("processing row", y)
        for x, cell in enumerate(row):
            is_cell_approachable = is_approachable(matrix, x, y)
            if is_cell_approachable:
                approachable_count += 1
                print(f"cell {y}{x} is approachable")

    return approachable_count


def update_and_count_matrix(matrix) -> int:
    print("next iteration...")
    next_matrix = deepcopy(matrix)

    approachable_count = 0

    for y, row in enumerate(matrix):
        print("processing row", y)
        for x, cell in enumerate(row):
            is_cell_approachable = is_approachable(matrix, x, y)
            if is_cell_approachable:
                approachable_count += 1
                next_matrix[y][x] = False
                print(f"cell {y}{x} is approachable")
    
    if approachable_count == 0:
        return 0
    
    return approachable_count + update_and_count_matrix(next_matrix)


def task_two():
    print("parsing input...")
    matrix = read_input()
    return update_and_count_matrix(matrix)


if __name__ == "__main__":
    count = task_two()
    print(f"count: {count}")

from itertools import pairwise
from math import prod

Matrix = list[str]

def read_input() -> Matrix:
    matrix = []
    for row in open("input.txt", "r"):
        matrix.append(
            row.replace("\n", "")
        )
    return matrix


def task_one():
    matrix = read_input()
    space_only_col_idxs: list[int] = []
    for x in range(0, len(matrix[0])):
        is_space_only = True
        for y in range(0, len(matrix)):
            if matrix[y][x] != " ":
                is_space_only = False
        if is_space_only:
            space_only_col_idxs.append(x)
    
    space_only_col_idxs = [-1, *space_only_col_idxs, len(matrix[0])]

    print(f"separators: {space_only_col_idxs}")

    result = 0

    for start, end in pairwise(space_only_col_idxs):
        print(f"start, end: {start}, {end}")
        numbers = []
        for row in matrix[:-1]:
            numbers.append(int(row[start+1:end].strip()))
        
        print(f"numbers: {numbers}")
        sign = matrix[-1][start+1:end].strip()
        print(f"sign: {sign}")
        if sign == "+":
            result += sum(numbers)
        elif sign == "*":
            result += prod(numbers)
        else:
            raise Exception("??")

    return result


def task_two():
    matrix = read_input()
    space_only_col_idxs: list[int] = []
    for x in range(0, len(matrix[0])):
        is_space_only = True
        for y in range(0, len(matrix)):
            if matrix[y][x] != " ":
                is_space_only = False
        if is_space_only:
            space_only_col_idxs.append(x)
    
    space_only_col_idxs = [0, *space_only_col_idxs, len(matrix[0])]

    print(f"separators: {space_only_col_idxs}")

    result = 0

    for start, end in pairwise(space_only_col_idxs):
        print(f"start, end: {start}, {end}")
        numbers = []
        for i in range(start, end):
            numbers.append("")
            for row in matrix[:-1]:
                numbers[-1] += row[i]
        
        print(f"raw numbers: {numbers}")

        numbers = [int(num) for num in numbers if bool(num.strip())]
        print(f"processed numbers: {numbers}")
        sign = matrix[-1][start:end].strip()
        print(f"sign: {sign}")
        if sign == "+":
            result += sum(numbers)
        else:
            result += prod(numbers)

    return result



if __name__ == "__main__":
    fresh_ingridients_count = task_two()
    print(f"fresh_ingridients_count: {fresh_ingridients_count}")

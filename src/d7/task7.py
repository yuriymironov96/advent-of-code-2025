from typing import Self, Tuple


Matrix = list[list[bool]]


def parse_input() -> Tuple[Matrix, int]:
    matrix: Matrix = []
    beam_origin_idx: int = None

    for row in open("input.txt"):
        if not beam_origin_idx and row.find("S"):
            beam_origin_idx = row.find("S")
        matrix.append([True if ch == "^" else False for ch in row.replace("\n", "")])

    return matrix, beam_origin_idx


def task_one():
    matrix, beam_origin_idx = parse_input()
    refraction_matrix: Matrix = []
    beams_above_idx: list[int] = [beam_origin_idx]

    repr = ""
    count_refractions = 0
    for y, row in enumerate(matrix):
        refraction_row = [False for col in row]
        refraction_matrix.append(refraction_row)
        for x, col in enumerate(row):
            if col and x in beams_above_idx:
                count_refractions += 1
                beams_above_idx = [el for el in beams_above_idx if el != x]
                if x - 1 >= 0:
                    beams_above_idx.append(x - 1)
                if x + 1 < len(refraction_row):
                    beams_above_idx.append(x + 1)

        repr += "".join(["^" if row[idx] else "|" if idx in beams_above_idx else "." for idx in range(0, len(row))]) + "\n"


    print(repr)

    return count_refractions


def task_two():
    matrix, beam_origin_idx = parse_input()
    refraction_matrix: Matrix = []
    beams_above_idx: list[int] = [beam_origin_idx]

    repr = ""
    count_refractions = 0
    for y, row in enumerate(matrix):
        refraction_row = [False for col in row]
        refraction_matrix.append(refraction_row)
        for x, col in enumerate(row):
            if col and x in beams_above_idx:
                count_refractions += 1
                beams_above_idx = [el for el in beams_above_idx if el != x]
                if x - 1 >= 0:
                    beams_above_idx.append(x - 1)
                if x + 1 < len(refraction_row):
                    beams_above_idx.append(x + 1)

        repr += "".join(["^" if row[idx] else "|" if idx in beams_above_idx else "." for idx in range(0, len(row))]) + "\n"


    print(repr)
    

    return count_refractions


if __name__ == "__main__":
    print("result", task_two())

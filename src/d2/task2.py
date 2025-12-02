from textwrap import wrap
from itertools import pairwise


def read_input() -> str:
    with open("input.txt", "r") as file:
        return file.read()


def is_invalid_id_one(id_candidate: int):
    str_repr = str(id_candidate)
    str_len = len(str_repr)
    return len(str_repr) % 2 == 0 and str_repr[:str_len//2] == str_repr[str_len//2:]


def task_one():
    text_input = read_input()
    id_candidate_ranges = text_input.split(",")
    invalid_id_sum = 0

    for id_candidate_range in id_candidate_ranges:
        start, end = id_candidate_range.split("-")
        for id_candidate in range(int(start), int(end)+1):
            if is_invalid_id_one(id_candidate):
                invalid_id_sum += id_candidate
                print(f"{id_candidate} is invalid")

    print(f"invalid id sum: {invalid_id_sum}")


def is_invalid_id_two(id_candidate: int):
    str_repr = str(id_candidate)
    str_len = len(str_repr)
    for len_candidate in range(1, (str_len // 2) + 1):
        parts = wrap(str_repr, len_candidate)
        if len(parts[0]) != len(parts[-1]):
            continue
        all_parts_equal = True
        for a, b in pairwise(parts):
            all_parts_equal = all_parts_equal and a == b
        if all_parts_equal:
            return True

    return False


def task_two():
    text_input = read_input()
    id_candidate_ranges = text_input.split(",")
    invalid_id_sum = 0

    for id_candidate_range in id_candidate_ranges:
        start, end = id_candidate_range.split("-")
        for id_candidate in range(int(start), int(end)+1):
            if is_invalid_id_two(id_candidate):
                invalid_id_sum += id_candidate
                print(f"{id_candidate} is invalid")

    print(f"invalid id sum: {invalid_id_sum}")


if __name__ == "__main__":
    # task_one()
    task_two()

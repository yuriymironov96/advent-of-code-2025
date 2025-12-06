from typing import Tuple

from itertools import product

NumberRange = Tuple[int, int]


FILLED_NEIGHBOURS_ALLOWED = 4


# ============== task one


def read_input() -> Tuple[list[NumberRange], list[int]]:
    fresh_ingridients: list[NumberRange] = []
    available_ingridients: list[int] = []

    parse_fresh_ingridients = True
    for row in open("input.txt", "r"):
        print(f"row {row}")
        row = row.replace("\n", "")
        if row.strip() == "":
            parse_fresh_ingridients = False
        elif parse_fresh_ingridients:
            begin, end = row.split("-")
            fresh_ingridients.append((int(begin), int(end)))
        else:
            # we can probably count the ingridients here and spare another cycle
            available_ingridients.append(int(row))

    return fresh_ingridients, available_ingridients


def task_one():
    fresh, available = read_input()

    fresh_confirmed = set()

    for available_item in available:
        for fresh_range in fresh:
            if available_item >= fresh_range[0] and available_item <= fresh_range[1]:
                print(f"available {available_item} is fresh")
                fresh_confirmed.add(available_item)

    return len(fresh_confirmed)


# ============== task two


# def eliminate_nested_ranges(fresh_ingridients: list[NumberRange]) -> list[NumberRange]:
#     idx_to_pop: list[int] = []
#     for a, b in product(range(0, len(fresh_ingridients)), repeat=2):
#         if a == b:
#             continue

#         start, end = fresh_ingridients[a]
#         m_start, m_end = fresh_ingridients[b]
#         if start >= m_start and end <= m_end and b not in idx_to_pop:
#             idx_to_pop.append(a)

#     idx_to_pop.sort(reverse=True)

#     for idx in idx_to_pop:
#         fresh_ingridients.pop(idx)
#     return fresh_ingridients

# def neighbour_merge(fresh_ingridients: list[NumberRange]) -> list[NumberRange]:
#     first_items = fresh_ingridients[:2]
#     if len(first_items) < 2:
#         return first_items
#     first, second = first_items
#     f_start, f_end = first
#     s_start, s_end = second

#     # (0, 9) (5, 11)
#     # (0, 9) (5, 9)
#     if f_end >= s_start and f_start <= s_start:
#         return [(min(f_start, s_start), max(f_end, s_end)), *neighbour_merge(fresh_ingridients[2:])]
#     else:
#         return [first, *neighbour_merge(fresh_ingridients[1:])]


# https://www.reddit.com/r/adventofcode/comments/1pemdwd/comment/nsl6elj/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
def task_two() -> int:
    fresh_ingridients: list[range] = []
    # fresh_ingridients_merged: list[NumberRange] = []
    for row in open("input.txt", "r"):
        print(f"row {row}")
        row = row.replace("\n", "")
        if row.strip() == "":
            break
        else:
            begin, end = row.split("-")
            fresh_ingridients.append(range(int(begin), int(end) + 1))


    fresh_ingridients.sort(key=lambda r: (r.start, r.stop))

    i = 0
    while i < len(fresh_ingridients):
        current_range = fresh_ingridients[i]
        j = i+1
        while j < len(fresh_ingridients):
            merge_candidate_range = fresh_ingridients[j]
            if merge_candidate_range.start <= current_range.stop:
                current_range = range(current_range.start, max(current_range.stop, merge_candidate_range.stop))
                fresh_ingridients[i] = current_range
                del fresh_ingridients[j]
            else:
                j += 1
        i += 1


    # fresh_ingridients = eliminate_nested_ranges(fresh_ingridients)

    # fresh_ingridients.sort(key=lambda r: r[0])
    # fresh_ingridients = neighbour_merge(fresh_ingridients)
    # fresh_ingridients.sort(key=lambda r: r[0])
    # fresh_ingridients = neighbour_merge(fresh_ingridients)
    # fresh_ingridients.sort(key=lambda r: r[0])
    # fresh_ingridients = neighbour_merge(fresh_ingridients)
    # fresh_ingridients.sort(key=lambda r: r[1])
    # fresh_ingridients = neighbour_merge(fresh_ingridients)
    # fresh_ingridients.sort(key=lambda r: r[1])
    # fresh_ingridients = neighbour_merge(fresh_ingridients)
    # fresh_ingridients.sort(key=lambda r: r[1])
    # fresh_ingridients = neighbour_merge(fresh_ingridients)
    

    return sum((r.stop - r.start) for r in fresh_ingridients)


if __name__ == "__main__":
    fresh_ingridients_count = task_two()
    print(f"fresh_ingridients_count: {fresh_ingridients_count}")

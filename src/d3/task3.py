from typing import Generator


def read_input() -> Generator[str]:
    for row in open("example.txt", "r"):
        yield row.replace("\n", "")


def get_largest_joltage(bank: str) -> int:
    # if bank == "811111111111119":
    #     import pdb;pdb.set_trace()
    # bank = list(bank_str)
    max_char_pos = 0
    for idx, char in enumerate(bank[:-1]):
        if int(char) > int(bank[max_char_pos]):
            max_char_pos = idx
    second_largest_char_pos = max_char_pos + 1
    for idx, char in enumerate(bank[max_char_pos + 1 :]):
        if int(char) > int(bank[second_largest_char_pos]):
            second_largest_char_pos = idx + max_char_pos + 1

    return int(bank[max_char_pos]) * 10 + int(bank[second_largest_char_pos])


def task_one():
    total_joltage = 0
    for bank in read_input():
        largest_joltage = get_largest_joltage(bank)

        total_joltage += largest_joltage
        print(f"row {bank} has max joltage {largest_joltage}")

    print(f"total joltage: {total_joltage}")


def get_largest_joltage_two(bank: str, look_before_depth: int = 12) -> str:

    searchable_part_of_string = bank[:len(bank)-look_before_depth]
    if not len(searchable_part_of_string):
        return ""
    max_char_pos = 0
    for idx, char in enumerate(searchable_part_of_string):
        if int(char) > int(searchable_part_of_string[max_char_pos]):
            max_char_pos = idx
    return searchable_part_of_string[max_char_pos] + get_largest_joltage_two(bank[max_char_pos:], look_before_depth-1)
    # # if bank == "811111111111119":
    # #     import pdb;pdb.set_trace()
    # # bank = list(bank_str)
    # max_char_pos = 0
    # for idx, char in enumerate(bank[:-1]):
    #     if int(char) > int(bank[max_char_pos]):
    #         max_char_pos = idx
    # second_largest_char_pos = max_char_pos + 1
    # for idx, char in enumerate(bank[max_char_pos + 1 :]):
    #     if int(char) > int(bank[second_largest_char_pos]):
    #         second_largest_char_pos = idx + max_char_pos + 1

    # return bank[max_char_pos] + get_largest_joltage_recursive()

def task_two():
    total_joltage = 0
    for bank in read_input():
        largest_joltage = get_largest_joltage_two(bank)

        total_joltage += int(largest_joltage)
        print(f"row {bank} has max joltage {largest_joltage}")

    print(f"total joltage: {total_joltage}")


if __name__ == "__main__":
    task_two()

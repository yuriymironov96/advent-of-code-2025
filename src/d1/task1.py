from typing import Generator


def read_input() -> Generator[str]:
    for row in open("input.txt", "r"):
        yield row


def get_effective_step(raw_step: str) -> int:
    direction = 1 if raw_step[0] == "R" else -1
    step = int(raw_step[1:])
    return step * direction


def part_one():
    current_position = 50
    current_counter_state = 0
    for row in read_input():
        effective_step = get_effective_step(row)
        current_position = (current_position + effective_step) % 100
        if current_position == 0:
            current_counter_state += 1
        print(
            f"after spinning {row}, position is {current_position} and counter state is {current_counter_state}"
        )

    print(f"final code: {current_counter_state}")


def part_two():
    current_position = 50
    current_counter_state = 0
    for row in read_input():
        row = row.replace("\n", "")
        effective_step = get_effective_step(row)
        if abs(effective_step) // 100 > 0:
            diff = abs(effective_step) // 100
            if 0 < effective_step < 100:
                diff -= 1
            current_counter_state += diff
        next_position = (current_position + effective_step) % 100
        if current_position + effective_step not in range(1, 100) and current_position != 0:
            current_counter_state += 1
        current_position = next_position
        print(
            f"after spinning {row}, position is {current_position} and counter state is {current_counter_state}"
        )

    print(f"final code: {current_counter_state}")


def part_two_bruteforce():
    """Emulate motion of a real safe wheel, tick by tick, counting how many times did it hit 0."""

    current_position = 50
    current_counter_state = 0
    for row in read_input():
        row = row.replace("\n", "")
        effective_step = get_effective_step(row)

        direction = 1 if effective_step > 0 else -1
        abs_effective_step = abs(effective_step)
        while abs_effective_step > 0:
            abs_effective_step -= 1
            current_position += 1 * direction
            if current_position % 100 == 0:
                current_counter_state += 1
        current_position %= 100

        print(
            f"after spinning {row}, position is {current_position} and counter state is {current_counter_state}"
        )
    print(f"final code: {current_counter_state}")


if __name__ == "__main__":
    part_two()

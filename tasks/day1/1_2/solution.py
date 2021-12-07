def load_input(filename: str = 'input') -> list[int]:
    with open(filename, 'r') as file:
        lines = [int(line.rstrip()) for line in file.readlines()]
    return lines


def get_sums(lines: list[int]) -> list[int]:
    return [sum(lines[i:i + 3]) for i in range(0, len(lines) - 2)]


def depth_increases(sums: list[int]) -> int:
    counter = 0
    prev = sums[0]

    for curr in sums[1:]:
        if curr > prev:
            counter += 1
        prev = curr

    return counter


def main():
    lines = load_input()
    sums = get_sums(lines)
    counter = depth_increases(sums)
    print(f'Number of depth increases: {counter}')


main()

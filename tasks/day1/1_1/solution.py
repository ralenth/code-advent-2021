def load_input(filename: str = 'input') -> list[int]:
    with open(filename, 'r') as file:
        lines = [int(line.rstrip()) for line in file.readlines()]
    return lines


def depth_increases(lines: list[int]) -> int:
    counter = 0
    prev = lines[0]

    for curr in lines[1:]:
        if curr > prev:
            counter += 1
        prev = curr

    return counter


def main():
    lines = load_input()
    counter = depth_increases(lines)
    print(f'Number of depth increases: {counter}')


main()

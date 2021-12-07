def load_input(filename: str = 'input') -> list[str]:
    with open(filename, 'r') as file:
        lines = [line.rstrip() for line in file.readlines()]
    return lines


def dive(lines: list[str]) -> int:
    position, depth = 0, 0

    for line in lines:
        cmd, x = line.split()
        if cmd == 'forward':
            position += int(x)
        elif cmd == 'up':
            depth -= int(x)
        else:
            depth += int(x)

    return position * depth


def main():
    lines = load_input()
    n = dive(lines)
    print(f'Position times depth is equal to: {n}')


main()

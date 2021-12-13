def load_input(filename: str = 'input') -> list:
    with open(filename, 'r') as file:
        lines = [line.rstrip() for line in file.readlines()]
        lines = [line.split(' | ')[1] for line in lines]
        digits = []
        for line in lines:
            digits.extend([len(digit) for digit in line.split()])
        return digits


def get_occurs(digits: list) -> dict:
    occurs = dict()
    for digit in digits:
        if digit not in occurs.keys():
            occurs[digit] = 1
        else:
            occurs[digit] += 1
    return occurs


def main():
    digits = load_input()
    occurs = get_occurs(digits)
    s = sum([occurs[i] for i in [2, 3, 4, 7]])
    print(f'Number of occurrences 1, 4, 7 and 8: {s}')


main()

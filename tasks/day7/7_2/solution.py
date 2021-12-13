def load_input(filename: str = 'input') -> list:
    with open(filename, 'r') as file:
        numbers = list(map(int, file.readlines()[0].rstrip().split(',')))
        return numbers


def cost(target: int, numbers: list) -> int:
    return sum([
        (abs(n - target) * (abs(n - target) + 1)) // 2 for n in numbers
    ])


def binsearch(numbers: list) -> int:
    start, end = 0, max(numbers)
    while start < end:
        middle = (start + end) // 2
        c1, c2, c3 = (
            cost(middle - 1, numbers), cost(middle, numbers), cost(middle + 1, numbers)
        )
        if c1 >= c2 and c2 <= c3:
            return c2
        elif c1 < c2:
            end = middle - 1
        elif c3 < c2:
            start = middle + 1

    return cost(start, numbers)


def main():
    numbers = load_input()
    fuel = binsearch(numbers)
    print(f'Fuel usage equals: {fuel}')


main()

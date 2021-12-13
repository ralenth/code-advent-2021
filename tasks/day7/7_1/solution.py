def load_input(filename: str = 'input') -> list:
    with open(filename, 'r') as file:
        return list(map(int, file.readlines()[0].rstrip().split(',')))


def fuel_usage(numbers: list) -> int:
    median = get_median(numbers)
    return sum([abs(x - median) for x in numbers])


def get_median(numbers: list) -> int:
    numbers = sorted(numbers)
    return numbers[(len(numbers) + 1) // 2]


def main():
    numbers = load_input()
    fuel = fuel_usage(numbers)
    print(f'Fuel usage equals: {fuel}')


main()

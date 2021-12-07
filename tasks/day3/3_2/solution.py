def load_input(filename: str = 'input') -> list[str]:
    with open(filename, 'r') as file:
        lines = [line.rstrip() for line in file.readlines()]
    return lines


def most_freq(numbers: list[str], idx: int) -> str:
    freq = ''.join(num[idx] for num in numbers)
    freq_1 = freq.count('1')
    if freq_1 >= (len(freq) / 2):
        return '1'
    return '0'


def choose_numbers(numbers: list[str], n: str, idx: int) -> list[str]:
    return [num for num in numbers if num[idx] == n]


def life_support(lines: list[str]) -> int:
    rating = {'oxygen': '', 'carbon': ''}

    for k in rating.keys():
        numbers = list(lines)
        i = 0

        while len(numbers) > 1:
            n = most_freq(numbers, i)
            if k == 'carbon':
                n = str(abs(1 - int(n)))
            numbers = choose_numbers(numbers, n, i)
            i += 1

        rating[k] = int(numbers[0], 2)

    return rating['oxygen'] * rating['carbon']


def main():
    lines = load_input()
    x = life_support(lines)
    print(f'Life support rating of the submarine: {x}')


main()

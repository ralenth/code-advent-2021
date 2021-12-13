def load_input(filename: str = 'input') -> dict:
    with open(filename, 'r') as file:
        fish = list(map(int, file.readlines()[0].rstrip().split(',')))
        fish_dict = {x: 0 for x in range(9)}
        for f in fish:
            fish_dict[f] += 1
        return fish_dict


def count_fish(days: int, fish: list) -> int:
    for _ in range(days):
        fish = update(fish)
    return sum(list(fish.values()))


def update(fish: dict) -> dict:
    for day, count in dict(fish).items():
        if day == 0:
            fish[8] += count
            fish[6] += count
            fish[0] = 0
        else:
            fish[day] -= count
            fish[day - 1] += count
    return fish


def main():
    fish = load_input()
    d = 80
    f = count_fish(d, fish)
    print(f'Number of fish after {d} days: {f}')


main()

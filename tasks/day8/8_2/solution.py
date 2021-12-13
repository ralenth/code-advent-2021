def load_input(filename: str = 'input') -> tuple[list, list]:
    with open(filename, 'r') as file:
        lines = [line.rstrip() for line in file.readlines()]
        lines = [line.split(' | ') for line in lines]
        in_digits, out_digits = [], []
        for line in lines:
            in_digits.append([set(digit) for digit in line[0].split()])
            out_digits.append([set(digit) for digit in line[1].split()])
        return in_digits, out_digits


def decode_easy(digits: list) -> tuple[dict, list, list]:
    decoded_digits = {}
    len_5, len_6 = [], []

    for digit in digits:
        if len(digit) == 2:
            decoded_digits['1'] = digit
        elif len(digit) == 3:
            decoded_digits['7'] = digit
        elif len(digit) == 4:
            decoded_digits['4'] = digit
        elif len(digit) == 7:
            decoded_digits['8'] = digit
        elif len(digit) == 5:
            len_5.append(digit)
        else:
            len_6.append(digit)

    return decoded_digits, len_5, len_6


def decode(digits: list) -> dict:
    decoded_digits, len_5, len_6 = decode_easy(digits)

    bd = decoded_digits['4'].difference(decoded_digits['7'])
    cf = decoded_digits['1']

    for digit in len_5:
        if len(bd.intersection(digit)) > 1:
            decoded_digits['5'] = digit
        elif len(cf.intersection(digit)) > 1:
            decoded_digits['3'] = digit
        else:
            decoded_digits['2'] = digit
    for digit in len_6:
        if len(bd.intersection(digit)) == 1:
            decoded_digits['0'] = digit
        elif len(cf.intersection(digit)) == 1:
            decoded_digits['6'] = digit
        else:
            decoded_digits['9'] = digit

    return decoded_digits


def sum_digits(in_digits: list, out_digits: list) -> int:
    s = 0
    for in_dig, out_dig in zip(in_digits, out_digits):
        decoded_digits = {
            ''.join(sorted(list(v))): k for k, v in decode(in_dig).items()
        }
        s_i = ''
        for d in out_dig:
            d = ''.join(sorted(list(d)))
            s_i += decoded_digits[d]
        s += int(s_i)

    return s


def main():
    in_digits, out_digits = load_input()
    s = sum_digits(in_digits, out_digits)
    print(f'Sum of all digits equals {s}')


main()

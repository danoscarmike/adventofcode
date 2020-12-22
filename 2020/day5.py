from helpers.input import str_array_from_list


def find_seat(seat_code, row=True):
    switcher = {
        "row": {"range": (0, 127), "code_range": (0, 7)},
        "seat": {"range": (0, 7), "code_range": (7, 10)},
    }

    search = "row"
    if not row:
        search = "seat"

    low = switcher[search]["range"][0]
    high = switcher[search]["range"][1]
    code_start = switcher[search]["code_range"][0]
    code_end = switcher[search]["code_range"][1]

    for i in range(code_start, code_end):
        dir = seat_code[i]
        if dir == "F" or dir == "L":
            if high - low == 1:
                return low
            high = high - ((high - low) // 2) - 1
        else:
            if high - low == 1:
                return high
            low = low + ((high - low) // 2) + 1
    return high


def get_seat_id(seat):
    return find_seat(seat) * 8 + find_seat(seat, False)


def part1(data):
    max_seat_id = 0
    for seat in data:
        seat_id = get_seat_id(seat)
        if seat_id > max_seat_id:
            max_seat_id = seat_id
    return max_seat_id


def part2(data):
    all_seats = []
    for seat in data:
        row = find_seat(seat)
        if row == 0 or row == 1:
            continue
        all_seats.append(get_seat_id(seat))
    for seat in all_seats:
        if (seat + 1) not in all_seats:
            return seat + 1
    return -1


if __name__ == "__main__":
    data = str_array_from_list("5.txt")
    print(part1(data))
    print(part2(data))

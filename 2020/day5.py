from helpers.input import str_array_from_list


def find_row(seat_code):
    low = 0
    high = 127
    for i in range(0, 7):
        fb = seat_code[i]
        if fb == "F":
            if high - low == 1:
                return low
            high = high - ((high - low) // 2) - 1
        else:
            if high - low == 1:
                return high
            low = low + ((high - low) // 2) + 1
    return high


def find_seat(seat_code):
    low = 0
    high = 7
    for i in range(7, 10):
        fb = seat_code[i]
        if fb == "L":
            if high - low == 1:
                return low
            high = high - ((high - low) // 2) - 1
        else:
            if high - low == 1:
                return high
            low = low + ((high - low) // 2) + 1
    return high


def get_seat_id(seat):
    return find_row(seat) * 8 + find_seat(seat)


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
        row = find_row(seat)
        if row == 0 or row == 127:
            continue
        else:
            seat_id = get_seat_id(seat)
            all_seats.append(seat_id)
    for id in all_seats:
        if (id + 1) not in all_seats:
            return id + 1
        if (id - 1) not in all_seats:
            return id - 1
    return -1


if __name__ == "__main__":
    data = str_array_from_list("5.txt")
    print(part1(data))
    print(part2(data))

from utilities import input


def count_race_winners(r: tuple[int]) -> int:
    count = 0
    duration, record = r
    for i in range(1, duration):
        distance = (duration - i) * i
        if distance > record:
            count = i
            break
    return duration - 2 * count + 1

def one(races: list[tuple[int]]) -> int:
    result = 1
    for r in races:
        result *= count_race_winners(r)
    return result


def concat_ints(d: list[int]) -> int:
    c = ""
    for i in d:
        c += str(i)
    return int(c)


def two(r: tuple[int]) -> int:
    return count_race_winners(r)


if __name__ == "__main__":
    data = input.str_array_from_list("6.txt")
    
    durations = [int(t) for t in data[0].split(":")[1].split()]
    distances = [int(d) for d in data[1].split(":")[1].split()]
    races = list(zip(durations, distances))

    print(f"Part 1: {one(races)}")

    duration = concat_ints(durations)
    distance = concat_ints(distances)
    race = (duration, distance)
    print(f"Part 2: {two(race)}")
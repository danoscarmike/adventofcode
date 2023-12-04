from utilities import input

cap = [12, 13, 14]

def one(data: dict) -> int:
    possible_games = []
    for key in data.keys():
        if data[key]["red"] <= 12:
            if data[key]["green"] <= 13:
                if data[key]["blue"] <= 14:
                    possible_games.append(key)
    return sum(possible_games)


def two(data: dict) -> int:
    set_powers = []
    for key in data.keys():
        power = 1
        for color in data[key].keys():
            power = power * data[key][color]
        set_powers.append(power)
            
    return sum(set_powers)


if __name__ == "__main__":
    data = input.str_array_from_list("2.txt")
    data_dict = {}
    colors = ["red", "green", "blue"]
    for game in data:
        game = game.split(":")
        game_id = int(game[0].split(" ")[-1])
        data_dict[game_id] = {"red":0, "green":0, "blue":0}
        selections = [s.strip() for s in game[1].split(";")]
        for selection in selections:
            cubes = [s.strip() for s in selection.split(",")]
            for set in cubes:
                for color in colors:
                    if set.endswith(color):
                        number = int(set.split(" ")[0])
                        if data_dict[game_id][color] < number:
                            data_dict[game_id][color] = number
                        break

    print(f"Part 1: {one(data_dict)}")
    print(f"Part 2: {two(data_dict)}")


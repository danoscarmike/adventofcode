def calculate_module_fuel(mass, module_fuel):
    mass = mass // 3 - 2
    if mass <= 0:
        return module_fuel
    else:
        module_fuel = module_fuel + mass
        return calculate_module_fuel(mass, module_fuel)


def fuel_counter_upper(input):
    total_fuel = 0
    for module_mass in input:
        total_fuel += calculate_module_fuel(module_mass, 0)
    return total_fuel


if __name__ == "__main__":
    import os

    path_to_input = os.getcwd() + "/input"
    input = []
    with open(path_to_input + "/1.txt", "r") as f:
        for line in f.readlines():
            input.append(int(line.rstrip()))
    print(fuel_counter_upper(input))

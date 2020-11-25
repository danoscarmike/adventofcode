import os


def intcode_computer(input):
    opcode_index = 0
    opcode = input[opcode_index]

    while opcode_index < (len(input) - 3) and opcode != 99:
        param_one = input[input[opcode_index + 1]]
        param_two = input[input[opcode_index + 2]]
        if opcode == 1:
            input[input[opcode_index + 3]] = param_one + param_two
        elif opcode == 2:
            input[input[opcode_index + 3]] = param_one * param_two
        else:
            raise os.error
        opcode_index += 4
        opcode = input[opcode_index]
    return input[0]


def gravity_assist(input):
    for noun in range(0, 100):
        for verb in range(0, 100):
            test_input = input.copy()
            test_input[1] = noun
            test_input[2] = verb
            try:
                if intcode_computer(test_input) == 19690720:
                    return 100 * noun + verb
            except os.error:
                continue
    return -1


if __name__ == "__main__":
    path_to_input = os.getcwd() + "/input"
    with open(path_to_input + "/2.txt", "r") as f:
        line = f.read()
        input = line.split(",")

    for x in range(0, len(input)):
        input[x] = int(input[x].rstrip())

    print(gravity_assist(input))

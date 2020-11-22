import os


def intcode_computer(input):
    opcode_index = 0
    opcode = input[opcode_index]

    while (opcode_index < (len(input) - 3) and opcode != 99):
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


if __name__ == "__main__":
    path_to_input = os.getcwd() + "/input"
    with open(path_to_input + "/2.txt", "r") as f:
        line = f.read()
        input = line.split(",")
    
    for x in range(0, len(input)):
        input[x] = int(input[x].rstrip())
    
    input[1] = 12
    input[2] = 2

    print(intcode_computer(input))

from helpers.input import str_array_from_list


def get_instructions(data):
    instructions = []
    for instr in data:
        tokens = instr.split(" ")
        instructions.append({"op": tokens[0], "arg": int(tokens[1])})
    return instructions


def check_for_loop(instructions):
    for i in instructions:
        i["count"] = 0
    accumulator = 0
    line = 0
    run = True
    success = False
    while run:
        if line >= len(instructions):
            print(f"Terminating ({accumulator})")
            success = True
            run = False
        elif line < 0:
            print(f"line out of range ({line})")
            run = False
        else:
            instr = instructions[line]
            print(instr)
            if instr["count"] >= 1:
                run = False
            elif instr["op"] == "nop":
                instr["count"] += 1
                line += 1
            elif instr["op"] == "acc":
                accumulator += instr["arg"]
                instr["count"] += 1
                line += 1
            else:
                instr["count"] += 1
                line += instr["arg"]
    return success, accumulator


def part1(data):
    instructions = get_instructions(data)
    _, accumulator = check_for_loop(instructions)
    return accumulator


def part2(data):
    instructions = get_instructions(data)
    for instr in instructions:
        if instr["op"] == "jmp":
            instr["op"] = "nop"
            success, acc = check_for_loop(instructions)
            if success:
                return acc
            else:
                instr["op"] = "jmp"
        elif instr["op"] == "nop":
            instr["op"] = "jmp"
            success, acc = check_for_loop(instructions)
            if success:
                return acc
            else:
                instr["op"] = "nop"
        else:
            continue
    return -1


if __name__ == "__main__":
    data = str_array_from_list("8.txt")
    print(part1(data))
    print(part2(data))

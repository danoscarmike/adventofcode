import itertools
import sys

sys.path.append("../utilities")

from utilities.input import read_rows_of_strings


def eval_l_to_r(operands):
    val = operands[0]
    for i in range(1, len(operands), 2):
        if operands[i] == "||":
            val = int(str(val) + str(operands[i + 1]))
        elif operands[i] == "+":
            val += operands[i + 1]
        elif operands[i] == "*":
            val *= operands[i + 1]
    return val


def is_solvable(val, operands, operators) -> bool:
    permutation_repeat = len(operands) - 1
    
    for i in itertools.product(operators, repeat=permutation_repeat):
        test_elements = [val for pair in zip(operands, i) for val in pair] + [operands[-1]]
        if val == eval_l_to_r(test_elements):
            return True
    return False


def solve(values, operands, operators) -> int:
    solvable = []
    for i, val in enumerate(values):
        if is_solvable(val, operands[i], operators):
            solvable.append(val)

    return sum(solvable)


if __name__ == "__main__":
    lines = read_rows_of_strings(sys.argv[1])
    values = [int(line.split()[0][0:-1]) for line in lines]
    operands = [[int(x.strip()) for x in line.split()[1:]] for line in lines]

    print(f"Part One: {solve(values, operands, ['*', '+'])}")
    print(f"Part Two: {solve(values, operands, ['+', '*', '||'])}")
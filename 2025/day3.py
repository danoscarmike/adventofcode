from utilities.input import read_rows_of_strings


def find_max_joltage(bank: str, number_of_batteries: int) -> int:
    if number_of_batteries == 2:
        max_joltage = 0
        for i in range(len(bank)):
            for j in range(i + 1, len(bank)):
                joltage = int(bank[i] + bank[j])
                if joltage > max_joltage:
                    max_joltage = joltage
        return max_joltage

    # For larger numbers of batteries, use a greedy approach
    # We need to keep exactly number_of_batteries digits to maximize the number
    digits_to_remove = len(bank) - number_of_batteries

    if digits_to_remove <= 0:
        return int(bank)

    # Use a stack to greedily keep larger digits
    stack = []
    for digit in bank:
        # While we can still remove digits and the current digit is larger than
        # the last digit in our result, remove the smaller digit
        while stack and digits_to_remove > 0 and digit > stack[-1]:
            stack.pop()
            digits_to_remove -= 1
        stack.append(digit)

    # If we still need to remove more digits, remove from the end
    while digits_to_remove > 0:
        stack.pop()
        digits_to_remove -= 1

    return int("".join(stack))


def solve(lines: list[str], number_of_batteries: int = 2) -> int:
    total = 0
    for line in lines:
        max_jolt = find_max_joltage(line, number_of_batteries)
        total += max_jolt
    return total


if __name__ == "__main__":
    lines = read_rows_of_strings("input/3.txt")
    print(solve(lines))
    print(solve(lines, number_of_batteries=12))

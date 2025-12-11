# Day 3 Part 1 SUCCESSFUL Solution

def calculate_joltage(bank):
    """Find the highest joltage in the given bank"""
    first = '0'
    second = '0'
    # Calculate the higest first digit
    # The last char will never be the highest first digit, so I omit it
    for num in bank[:-1]:
        if int(num) > int(first):
            first = num

    # Base our search for the highest second digit forward from the index of the first digit
    first_index = bank.find(first)
    for num in bank[first_index + 1:]:
        if int(num) > int(second):
            second = num

    return first + second

def main():
    joltages = []
    with open('input.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            joltages.append(int(calculate_joltage(line)))
    print(sum(joltages))


if __name__ == "__main__":
    main()

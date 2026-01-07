# Day 6 Part 2 Successful Solution

# NOTE: There is probably a better way to solve matrices math than this
# but hey, it works.

def solve_math_p2(input):
    """My janky-ass solution to solve some oddly structured math"""
    total_sum = 0
    num_list = []
    operator = ''
    for i, tup in enumerate(input):
        if tup[-1] == '+' or tup[-1] == '*':
            operator = tup[-1]
            tup = tup[:-1]
        num = ''
        for val in tup:
            num += val.strip()
        # See if we are at the problem separator (tuple filled with spaces in this case)
        # Which I strip above, so will be an empty string
        if num == '':
            if operator == '+':
                total_sum += sum(num_list)
            else:
                problem_total = 1
                # Reverse the list so we multiply right to left
                for val in num_list[::-1]:
                    problem_total *= val
                total_sum += problem_total

            num_list = []
        else:
            num_list.append(int(num))

            # Check to see if we are on the last iteration
            # We don't have the space delimiter at the end
            if i == (len(input) - 1):
                if operator == '+':
                    total_sum += sum(num_list)
                else:
                    problem_total = 1
                    # Reverse the list so we multiply right to left
                    for val in num_list[::-1]:
                        problem_total *= val
                    total_sum += problem_total

    return total_sum


def process_input_p2(input_file):
    """
    Pair each value by column within a tuple, creates a list of these tuples.
    """
    # For part 2, need to capture positional white space of each num
    rows = []
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            rows.append(list(line.rstrip('\n')))

    # '*' operator unpacks the list of lists, passing each to zip() as arguments
    return list(zip(*rows))

def main():
    input = process_input_p2("input.txt")
    total_sum = solve_math_p2(input)
    print(total_sum)


if __name__ == "__main__":
    main()

# This is my SUCCESSFUL solution to Day 1 Part 1

def dial(arrow, rotation):
    """
    50 - 68 --> 82    0 - 5 --> 95
    # Range(100)
    """
    direction, num = rotation[0], int(rotation[1:])

    # Deal with cases where num is large
    if num not in range(100):
        num = int(str(num)[-2:])

    if direction == 'L':
        arrow = range(100)[arrow - num]
    if direction == 'R':
        if arrow + num >= 100:
            arrow = (arrow + num) - 100
        else:
            arrow = arrow + num

    return arrow

def main():
    zero_count = 0
    arrow = 50
    with open("input.txt", "r", encoding="utf-8") as f:
        for line in f:
            #print(line, end='')
            arrow = dial(arrow, line)
            if arrow == 0:
                zero_count += 1
    print(zero_count)

if __name__ == "__main__":
    main()

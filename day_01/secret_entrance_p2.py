# day 1 part 2 SUCCESSFUL solution

def dial2(arrow, rotation):
    """
    50 - 68 --> 82    0 - 5 --> 95
    Dial values represented by `range(100)`
    """
    direction, num = rotation[0], int(rotation[1:])
    zeros = 0
    # Deal with cases where num is > 100 and account for extra zero passes
    if num not in range(100):
        zeros += (num // 100)
        num = int(str(num)[-2:]) # Alternatively could have used modulo here
        # num = num % 100

    if direction == 'L':
        # Don't count zero passes when the arrow starts at 0
        if num > arrow and arrow != 0:
            zeros += 1
        arrow = range(100)[arrow - num]
        # or `(arrow - num) % 100` when num > arrow
        # would need more conditionals like "R" below

    if direction == 'R':
        if arrow + num > 100:
            arrow = (arrow + num) - 100 # or (arrow + num) % 100
            zeros += 1
        elif arrow + num == 100:
            arrow = 0
        else:
            arrow = arrow + num

    return zeros, arrow

def main():
    zero_count = 0
    arrow = 50
    with open("input.txt", "r", encoding="utf-8") as f:
        for line in f:
            #print(line, end='')
            zeros, arrow = dial2(arrow, line)
            zero_count += zeros
            if arrow == 0:
                zero_count += 1
    print(zero_count)

if __name__ == "__main__":
    main()

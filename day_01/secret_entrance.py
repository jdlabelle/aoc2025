
def dial(rotation):
    zero_count = 0
    arrow = 50
    direction, num = rotation[0], int(rotation[1:])

    # There is probably a better way to do this that the constant type conversion. First pass though.
    if direction == 'L':
        if arrow - num < 0:
            diff = str(arrow - num)
            arrow = int(diff[-2:])
            if arrow == 0:
                zero_count += 1
        else:
            arrow = arrow - num
            if arrow == 0:
                zero_count += 1

    if direction == 'R':
        if arrow + num > 99:
            sum = str(arrow + num)
            arrow = int(sum[-2:])
            if arrow == 0:
                zero_count += 1
        else:
            arrow = arrow + num
            if arrow == 0:
                zero_count += 1

def main():
    with open("input.txt", "r", encoding="utf-8") as f:
        for line in f:
            print(line, end='')

if __name__ == "__main__":
    main()

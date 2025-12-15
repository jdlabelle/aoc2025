# Day 4 Part 1
def paper_access(position):
    pass

    # Node connections:
    # For Node `n` at position (1,1) (2nd list, 2nd item in the list)
    # (1,0), (1,2)  Same Line
    # (0,0), (0,1), (0,2)  Above
    # (2, 0), (2,1), (2,2) Below
    # Check each position relative to the node to see if they contain an `@` symbol
    # if total number of `@` < 4, the roll can be accessed --> `count += 1`

def main():
    grid = []
    with open('input.txt', 'r', encoding='utf-8') as f:
        for line in f:
            grid.append(list(line.strip()))
    print(len(grid[1]))


if __name__ == "__main__":
    main()

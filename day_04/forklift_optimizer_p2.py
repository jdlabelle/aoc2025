# Day 4 Part 2 Successful Solution

def extract_paper_p2(grid):
    """
    Iterate through each node in the grid to find paper and determine if 
    accessible. Remove each accessible paper and rerun the loop until no
    additional accessible papers are found. Return the total number of
    accessible paper.
    """
    total_accessible_rolls = 0

    # all rows are the same length in the grid
    y_len = len(grid)    # Row: Y-Axis
    x_len = len(grid[0])    # Column: X-Axis
    
    while True:
        loop_roles = 0
        for y in range(y_len):
            for x in range(x_len):
                if grid[y][x] == '@':
                    paper_neighbors = get_neighbors(grid, y, x)
                    if paper_neighbors < 4:
                        loop_roles += 1
                        # Remove the roll / update the node
                        grid[y][x] = '.'

        # if no accessible rolls are found, break out of the while loop
        if loop_roles == 0:
            break
        else:
            total_accessible_rolls += loop_roles

    return total_accessible_rolls

def get_neighbors(grid, row, col):
    """Find the number of neighboring paper rolls of a roll of paper"""
    paper_neighbors = 0

    # First conditional checks for edges (out-of-bounds)
    # cardinals
    if (col - 1) >= 0:
        if grid[row][col - 1] == '@':
            paper_neighbors += 1
    if (col + 1) < len(grid[0]):
        if grid[row][col + 1] == '@':
            paper_neighbors += 1
    if (row - 1) >= 0:
        if grid[row - 1][col] == '@':
            paper_neighbors += 1
    if (row + 1) < len(grid):
        if grid[row + 1][col] == '@':
            paper_neighbors += 1

    # diagonals
    if (row - 1) >= 0 and (col - 1) >= 0:
        if grid[row - 1][col - 1] == '@':
            paper_neighbors += 1
    if (row - 1) >= 0 and (col + 1) < len(grid[0]):
        if grid[row - 1][col + 1] == '@':
            paper_neighbors += 1
    if (row + 1) < len(grid) and (col - 1) >= 0:
        if grid[row + 1][col - 1] == '@':
            paper_neighbors += 1
    if (row + 1) < len(grid) and (col + 1) < len(grid[0]):
        if grid[row + 1][col + 1] == '@':
            paper_neighbors += 1

    return paper_neighbors

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
    rolls = extract_paper_p2(grid)
    print(rolls)


if __name__ == "__main__":
    main()

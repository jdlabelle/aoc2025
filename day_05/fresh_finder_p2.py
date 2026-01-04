# Day 5 Part 2 Successful Solution
import re

# This was a great problem to learn how to merge / combine large ranges of numbers
# in a memory-efficient way. Required a much different approach than part 1.

def find_fresh_p2(range_lst: list[tuple]) -> int:
    """
    Intake a list of fresh ingredient ranges, merge the ranges that overlap,
    and compute the total fresh ingredients represented by the ranges.
    """
    range_lst.sort(key=lambda interval: interval[0])
    # sorting makes interval[0] always <= next_interval[0]
    merged = [range_lst[0]]

    for current in range_lst[1:]:
        # Check if the current interval overlaps with the last merged interval.
        # This is done by seeing if the start of the current interval is less 
        # than or equal to the end of the last merged interval.
        if current[0] <= merged[-1][1]:
            # Overlap, merge the intervals:
            merged[-1] = (merged[-1][0], max(current[1], merged[-1][1]))
        else:
            # if no overlap, add the range to the end of the merged list
            merged.append(current)

    fresh_count = 0
    for interval in merged:
        start, end = interval
        fresh_count += (end + 1) - start

    return fresh_count

def process_input_p2(input_file):
    """
    Parse input file to capture fresh ingredient ranges. The ranges are
    converted into tuples for easy processing in find_fresh_p2.
    """
    range_lst = []

    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            match = re.match(r"^(\d+)-(\d+)$", line)
            if match:
                range_lst.append((int(match.group(1)), int(match.group(2))))

    return range_lst

def main():
    ranges = process_input_p2("input.txt")
    result = find_fresh_p2(ranges)
    print(result)


if __name__ == '__main__':
    main()

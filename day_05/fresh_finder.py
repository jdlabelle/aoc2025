# Day 5 Part 1 Successful Solution 
import re

def find_fresh(range_lst: list[tuple], ingredients: list[int]) -> int:
    """Find the fresh ingredients"""
    fresh_set = set()
    for ingredient in ingredients:
        for rng in range_lst:
            start, end = rng
            if ingredient in range(start, end + 1):
                fresh_set.add(ingredient)
                
    return len(fresh_set)

def process_input(input_file):
    """
    Parse input file to capture fresh ingredient ranges and available
    ingredients into two separate lists and return them. The ranges are
    converted into tuples for easy processing in find_fresh.
    """
    range_lst = []
    ingredients = []

    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            match = re.match(r"^(\d+)-(\d+)$", line)
            if match:
                range_lst.append((int(match.group(1)), int(match.group(2))))
            elif re.match(r"^\d+$", line):
                ingredients.append(int(line.strip()))

    # print(range_lst)
    # print("--------BREAK---------")
    # print(ingredients)

    return range_lst, ingredients

def main():
    ranges, items = process_input("input.txt")
    result = find_fresh(ranges, items)
    print(result)


if __name__ == '__main__':
    main()

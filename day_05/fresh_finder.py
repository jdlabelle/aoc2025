# Day 5 Part 1
import re

def find_fresh(range_lst: list[str], ingredients: list[str]) -> int:

    return 1

def process_input(input_file):
    """
    Parse input file to capture fresh ingredient ranges and available
    ingredients into two separate lists and return them.
    """
    range_lst = []
    ingredients = []

    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            if re.match(r"^\d+[-]\d+$", line):
                range_lst.append(line.strip())
            elif re.match(r"^\d+$", line):
                ingredients.append(line.strip())

    # print(range_lst)
    # print("--------BREAK---------")
    # print(ingredients)

    return range_lst, ingredients

def main():
    process_input("test_input.txt")

if __name__ == '__main__':
    main()

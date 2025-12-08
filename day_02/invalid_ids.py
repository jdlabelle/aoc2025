import re

# Day 2 Part 1

def find_invalid_ids(id_range: str) -> list[int]:
    # Start by processing the input string into its range of numbers
    m = re.match(r"^(\d+)-(\d+)$", id_range)
    range_start = int(m.group(1))
    range_stop = int(m.group(2)) + 1
    #print(list(range(range_start, range_stop)))

    # Find the invalid ids in the range
    invalid_ids = []
    for num in range(range_start, range_stop):
        if str(num).startswith('0'):
            continue
        # Match num using the index of the middle to check if it repeats
        num_length = len(str(num))
        if num_length % 2 == 0: # invalid IDs always have an even length
            repeat_index = num_length // 2
            if str(num)[:repeat_index] in str(num)[repeat_index:]:
                invalid_ids.append(num)

    return invalid_ids

def main():
    with open("input.txt", 'r', encoding='utf-8') as f:
        data = f.read()
    range_lst = data.strip().split(',')
    #print(range_lst)
    invalids = find_invalid_ids("998-1012")
    print(invalids)

if __name__ == "__main__":
    main()

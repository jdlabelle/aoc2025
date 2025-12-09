import re

# Day 2 Part 2
def find_invalid_ids_p2(id_range: str) -> list[int]:
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
        # Change to loop through chars at index to see if they repeat
        # for i in str(num)
        # if str(num)[i] in str(num)[i+1]:
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

    invalid_id_lst = []
    breakpoint()
    for id_range in range_lst:
        invalid_id_lst.extend(find_invalid_ids_p2(id_range))
    print(sum(invalid_id_lst))

if __name__ == "__main__":
    main()

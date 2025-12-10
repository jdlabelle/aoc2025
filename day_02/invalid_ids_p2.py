import re

# Day 2 Part 2 SUCCESSFUL solution
def factorize(num: int) -> list[int]:
    """Find the factors of a number"""
    factors = []
    for x in range(1, num+1):
        if num % x == 0:
            factors.append(x)
    # remove the number itself as invalids need to appear at least twice
    factors.pop()
    return factors

def find_invalid_ids_p2(id_range: str) -> list[int]:
    # Start by processing the input string into its range of numbers
    m = re.match(r"^(\d+)-(\d+)$", id_range)
    range_start = int(m.group(1))
    range_stop = int(m.group(2)) + 1
    #print(list(range(range_start, range_stop)))

    # Find the invalid ids in the range
    invalid_ids = []
    # invalids never start with zero
    for num in range(range_start, range_stop):
        if str(num).startswith('0'):
            continue
        # An invalid sequence (amount of times a number repeats)
        # is a factor of the length of the number
        num_length = len(str(num))
        factors = factorize(num_length)
        for factor in factors:
            if str(num)[:factor] * (num_length // factor) == str(num):
                invalid_ids.append(num)
                # end search once an invalid is identified
                break

    return invalid_ids

def main():
    with open("input.txt", 'r', encoding='utf-8') as f:
        data = f.read()
    range_lst = data.strip().split(',')

    invalid_id_lst = []
    for id_range in range_lst:
        invalid_id_lst.extend(find_invalid_ids_p2(id_range))
    print(sum(invalid_id_lst))

if __name__ == "__main__":
    main()

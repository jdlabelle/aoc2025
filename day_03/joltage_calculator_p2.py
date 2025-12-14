# Day 3 Part 2 

def calculate_joltage_p2(bank):
    """Find the highest joltage in the given bank"""

    bank_lst = list(bank)
    batteries = []
    index = 0
    # fsearch_index = 0

    first = '0'
    second = '0'
    third = '0'
    fourth = '0'
    # Calculate the higest first digit
    for i, num in enumerate(bank_lst[:-11]):
        if int(num) > int(first):
            first = num
            index = i + 1
    bank_lst = bank_lst[index:]
    batteries.append(first)

    # Base our search for the highest second digit forward from the index of the first digit
    for i, num in enumerate(bank_lst[:-10]):
        if int(num) > int(second):
            second = num
            index = i + 1
    bank_lst = bank_lst[index:]
    batteries.append(second)

    for i, num in enumerate(bank_lst[:-9]):
        if int(num) > int(third):
            third = num
            index = i + 1
    bank_lst = bank_lst[index:]
    batteries.append(third)

    for i, num in enumerate(bank_lst[:-8]):
        if int(num) > int(fourth):
            fourth = num
            index = i + 1
    bank_lst = bank_lst[index:]
    batteries.append(fourth)

    print(batteries)
    return first + second + third + fourth
    #
    # for battery_number in range(12):
    #     battery = 0
    #     for i, num in enumerate(bank_lst):
    #         # print(i, num)
    #         if i 
    #         if num in bank_lst[fsearch_index:-(11 - battery_number)]:
    #             if int(num) > int(battery):
    #                 battery = num
    #                 fsearch_index = i + 1 #3
    #     batteries.append(battery)
    #
    # return batteries



    # batteries = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
    # Calculate the higest first digit
    # The first number will never be in the last 11 digits 
    #breakpoint()
    # bank_index = 0
    #for index, battery in enumerate(batteries):
        #for i, num in enumerate(bank[bank_index:-(11-index)]):
    # for x in range(12):
    #     print(f"battery_number: {x}")
    #     battery = 0
    #     for i, num in enumerate(bank[bank_index:-(11-x)]):
    #         if int(num) > int(battery):
    #             battery = num
    #             bank_index = i + 1
    #             print(f"bank_index: {bank_index}, battery: {battery}")
    #     batteries.append(battery)
    #
    # return batteries

def main():
    # joltages = []
    # with open('input.txt', 'r', encoding='utf-8') as f:
    #     for line in f:
    #         line = line.strip()
    #         joltages.append(int(calculate_joltage_p2(line)))
    #print(sum(joltages))
    print(calculate_joltage_p2("234234234234278"))


if __name__ == "__main__":
    main()

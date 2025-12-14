# Day 3 Part 2 SUCCESSFUL solution

def calculate_joltage_p2(bank):
    """Find the highest joltage in the given bank, now with 12 batteries"""
    bank_lst = list(bank)
    batteries = []
    f_index = 0

    for bat_num in range(12):
        battery = '0'
        # when we need to get the final battery
        if bat_num == 11:
            for num in bank_lst:
                if int(num) > int(battery):
                    battery = num
            batteries.append(battery)
        # Batteries 1-11
        else:
            for i, num in enumerate(bank_lst[:-(11 - bat_num)]):
                if int(num) > int(battery):
                    battery = num
                    f_index = i + 1
            # Shorten the list after each battery
            # Next iteration starts the search at the next number forward of the selected battery
            bank_lst = bank_lst[f_index:]
            batteries.append(battery)

    return "".join(batteries)

    # This was my proof of concept working out the pattern

    # first = '0'
    # second = '0'
    # third = '0'
    # fourth = '0'
    # # Calculate the higest first digit
    # for i, num in enumerate(bank_lst[:-11]):
    #     if int(num) > int(first):
    #         first = num
    #         index = i + 1
    # bank_lst = bank_lst[index:]
    # batteries.append(first)
    #
    # # Base our search for the highest second digit forward from the index of the first digit
    # for i, num in enumerate(bank_lst[:-10]):
    #     if int(num) > int(second):
    #         second = num
    #         index = i + 1
    # bank_lst = bank_lst[index:]
    # batteries.append(second)
    #
    # for i, num in enumerate(bank_lst[:-9]):
    #     if int(num) > int(third):
    #         third = num
    #         index = i + 1
    # bank_lst = bank_lst[index:]
    # batteries.append(third)
    #
    # for i, num in enumerate(bank_lst[:-8]):
    #     if int(num) > int(fourth):
    #         fourth = num
    #         index = i + 1
    # bank_lst = bank_lst[index:]
    # batteries.append(fourth)
    #
    # print(batteries)
    # return first + second + third + fourth

def main():
    joltages = []
    with open('input.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            joltages.append(int(calculate_joltage_p2(line)))
    print(sum(joltages))

if __name__ == "__main__":
    main()

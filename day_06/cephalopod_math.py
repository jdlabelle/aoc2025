# Day 6 Part 1 Successful Solution

def solve_math(input):
    sum = 0
    for problem in input:
        operator = problem[-1]
        if operator == '+':
            res = 0 
            for num in problem[:-1]:
                res += int(num)
            sum += res
        elif operator == '*':
            res = int(problem[0])
            for num in problem[1:-1]:
                res *= int(num)
            sum += res
        else:
            raise ValueError("unexpected operator")
        
    return sum

def process_input(input_file):
    rows = []
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            rows.append(line.split())

    # '*' operator unpacks the list of lists, passing each to zip() as arguments
    return list(zip(*rows))
            

def main():
    input = process_input("input.txt")
    total_sum = solve_math(input)
    print(total_sum)

if __name__ == "__main__":
    main()

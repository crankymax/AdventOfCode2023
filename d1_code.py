from io import StringIO

def part_1():
    # part 1
    test_data = """1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet
    """

    #input_src = StringIO(test_data)
    input_src = open('d1_input.txt')

    dig_sum = 0

    # Day 1
    for line in input_src:
        digits = list(filter(str.isdigit, line))
        dig_sum += int(digits[0] + digits[-1])

    print(dig_sum)

def part_2():
    # part 2
    test_data = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

    #input_src = StringIO(test_data)
    input_src = open('d1_input.txt')
    alph_digits = {"one": '1', "two": '2', "three": '3', "four": '4', "five": '5',
                   "six": '6', "seven": '7', "eight": '8', "nine": '9'}

    key_set = set(alph_digits.keys())
    min_key = 3
    max_key = 5
    dig_sum = 0
    for line in input_src:
        strt = 0
        end = min_key
        digi_vals = []
        while strt < len(line):
            if line[strt].isdigit():
                #print(line[strt])
                digi_vals.append(line[strt:strt+1])
                strt += 1
                end += 1
            elif line[strt:end] in key_set:
                #print(line[strt:end])
                digi_vals.append(alph_digits[line[strt:end]])
                strt += 1
                end = strt + min_key
            elif (end-strt) < max_key:
                # try another char
                end += 1
            else:
                # we didn't find an int val or char int so inc start and set end to start + 3
                strt += 1
                end = strt + min_key
        print(digi_vals[0] + digi_vals[-1], digi_vals, line)
        dig_sum += int(digi_vals[0] + digi_vals[-1])

    print(dig_sum)

if __name__ == '__main__':
    #part_1()
    part_2()
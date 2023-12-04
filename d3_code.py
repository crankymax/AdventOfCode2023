from io import StringIO


def find_symbols(line):
    all_ind = []
    for sym in "*#+-&/=%$@":
        index = 0
        while index != -1:
            index = line.find(sym, index+1)
            if index != -1:
                all_ind.append(index)
    return all_ind


def get_nr_digs(line, col, engine):
    l_start = (line-1) if line > 0 else line
    l_end = (line+1) if line < len(engine) else line
    c_start = (col-1) if col > 0 else col
    c_end = (col+1) if col < len(engine[0]) else col
    digits = []
    for ln in range(l_start, l_end+1):
        for cl in range(c_start, c_end+1):
            # print(f'l:{ln}-c:{cl} isdig{engine[ln][cl]}{engine[ln][cl].isdigit()}')
            if engine[ln][cl].isdigit():
                digits.append((ln, cl))

    return digits


def part_near(chk_pnt, engine):
    # we need to keep reading digits to left and right of chk_pnt
    min_col = chk_pnt[1]
    while min_col > 0:
        if engine[chk_pnt[0]][min_col-1].isdigit():
            min_col -= 1
        else:
            break

    max_col = chk_pnt[1]
    while max_col < len(engine[0])-1:
        if engine[chk_pnt[0]][max_col+1].isdigit():
            max_col += 1
        else:
            break
    print(f'start-end:{min_col}:{max_col} value {engine[chk_pnt[0]][min_col:max_col+1]}')
    return ((chk_pnt[0], min_col), engine[chk_pnt[0]][min_col:max_col+1])

def part_1():
    # part 1
    test_data = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

    #input_src = StringIO(test_data)
    input_src = open('d3_input.txt')

    engine_schematic = list()
    symbol_map = list()

    for line in input_src:
        engine_schematic.append(line.strip())
        symbol_map.append(find_symbols(engine_schematic[-1]))

    print(symbol_map)
    # print(engine_schematic)
    parts = dict()
    for line, cols in enumerate(symbol_map):
        for col in cols:
            print(f'lc:{line}:{col} {engine_schematic[line][col]} ')
            digits = get_nr_digs(line, col, engine_schematic)
            print(digits)
            for chk_pnt in digits:
                pos, part_num = part_near(chk_pnt, engine_schematic)
                parts[pos] = part_num
    print(parts)
    part_sum = sum([int(x) for x in parts.values()])
    print(f'\nParts sum {part_sum}\n')


def part_2():
    # part 2
    test_data = """467..114..
    ...*......
    ..35..633.
    ......#...
    617*......
    .....+.58.
    ..592.....
    ......755.
    ...$.*....
    .664.598.."""

    #input_src = StringIO(test_data)
    input_src = open('d3_input.txt')

    gear_ratio_sum = 0
    engine_schematic = list()
    symbol_map = list()

    for line in input_src:
        engine_schematic.append(line.strip())
        symbol_map.append(find_symbols(engine_schematic[-1]))

    print(symbol_map)

    for line, cols in enumerate(symbol_map):
        for col in cols:
            print(f'lc:{line}:{col} {engine_schematic[line][col]} ')
            if engine_schematic[line][col] != '*':
                continue

            parts = dict()
            digits = get_nr_digs(line, col, engine_schematic)
            print(digits)
            for chk_pnt in digits:
                pos, part_num = part_near(chk_pnt, engine_schematic)
                parts[pos] = part_num
            if len(parts.values()) == 2:
                gears = list(parts.values())
                gear_ratio_sum += int(gears[0]) * int(gears[1])
    print(gear_ratio_sum, '\n')


if __name__ == '__main__':
    #part_1()
    part_2()


from io import StringIO
from collections import Counter, defaultdict


def part_1():
    # part 1
    test_data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

    #input_src = StringIO(test_data)
    input_src = open('d2_input.txt')

    game_sum = 0

    for line in input_src:
        game_id, sets = line.split(':')
        game_id = game_id.split(' ')[-1]
        print(game_id)
        good_game = True
        for game_set in sets.split(';'):
            cube_count = Counter()
            for num_colour in game_set.split(','):
                num, colour = num_colour.strip().split(' ')
                cube_count.update({colour: int(num)})
            if cube_count['red'] > 12 or cube_count['green'] > 13 or cube_count['blue'] > 14:
                print(cube_count)
                good_game = False
        if good_game:
            print(f'Good_game {game_id}\n')
            game_sum += int(game_id)

        print(line.strip(), '\n')

    print(game_sum)

def part_2():
    # part 2
    test_data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

    #input_src = StringIO(test_data)
    input_src = open('d2_input.txt')

    power_sum = 0

    for line in input_src:
        game_id, sets = line.split(':')
        game_id = game_id.split(' ')[-1]
        print(game_id)
        print(line.strip())
        cube_max = {'red': 0, 'green': 0, 'blue': 0}
        for game_set in sets.split(';'):
            for num_colour in game_set.split(','):
                num, colour = num_colour.strip().split(' ')
                cube_max[colour] = max(int(num), cube_max[colour])

        power = cube_max['blue'] * cube_max['red'] * cube_max['green']
        power_sum += power
        print(f'powers {cube_max}={power}')


    print(power_sum, '\n')


if __name__ == '__main__':
    #part_1()
    part_2()

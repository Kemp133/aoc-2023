from typing import Dict
from shared import parse_colours_and_quantities, get_game_id_and_line


def solve(game_line: str) -> int:
    games = [game.strip() for game in game_line.split(";")]

    # Create a dictionary to store max value found for current colour
    max_colour_count = {}

    for cur_game in games:
        colours = parse_colours_and_quantities(cur_game)

        # For every key in the configuration, make sure the quantity from the game for that colour is less than that of
        # the configuration value
        for key in colours:
            # Put values into local variables to prevent multiple accesses for the values
            max_colour_count_val, colours_val = max_colour_count.get(key), colours[key]

            # If the colour doesn't already exist in the colours count dictionary, add it with the current value for
            # that colour
            if not max_colour_count_val:
                max_colour_count[key] = colours_val
            # Otherwise, if the current colour value is greater than the currently recorded maximum value, set the
            # maximum value to the current colour value
            elif max_colour_count_val < colours_val:
                max_colour_count[key] = colours[key]

    # Calculate the product of the values
    product = 1
    for value in max_colour_count.values():
        product = product * value

    # Finally, return the product of the values of the colours
    return product


def main():
    # Sum variable
    id_product_sum = 0
    with open("input.txt") as problem:
        for game in problem:
            _, game_line = get_game_id_and_line(game)

            # If the game is valid (i.e. all sub games are valid), then add the ID for this game to the total
            id_product_sum += solve(game_line)

    print(id_product_sum)


def test():
    print(solve("3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"))
    print(solve("1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"))
    print(solve("8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"))
    print(solve("1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"))
    print(solve("6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"))


if __name__ == '__main__':
    main()
    # test()

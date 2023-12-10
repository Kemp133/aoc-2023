from typing import Dict
from .shared import parse_colours_and_quantities, get_game_id_and_line


def solve(game_line: str, configuration: Dict[str, int]) -> bool:
    games = [game.strip() for game in game_line.split(";")]

    for cur_game in games:
        colours = parse_colours_and_quantities(cur_game)

        # If the keys of colours isn't a subset of the keys of configuration (i.e. at least all of the keys in the
        # configuration dictionary are present in the colours dictionary), then return False early as these are not
        # comparable data sets
        if not set(colours.keys()).issubset(set(configuration.keys())):
            return False

        # For every key in the configuration, make sure the quantity from the game for that colour is less than that of
        # the configuration value
        for key in colours:
            if colours[key] > configuration[key]:
                return False

    # If we get here, the games are all valid, so return true
    return True


def main():
    # Sum variable
    id_sum = 0
    with open("input.txt") as problem:
        for game in problem:
            game_id, game_line = get_game_id_and_line(game)

            # If the game is valid (i.e. all sub games are valid), then add the ID for this game to the total
            if solve(game_line, {"red": 12, "green": 13, "blue": 14}):
                id_sum += int(game_id)

    print(id_sum)


def test():
    config = {"red": 12, "green": 13, "blue": 14}
    print(solve("3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", config))
    print(solve("1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", config))
    print(solve("8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", config))
    print(solve("1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", config))
    print(solve("6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", config))


if __name__ == '__main__':
    main()

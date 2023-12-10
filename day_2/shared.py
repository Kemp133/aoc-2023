from typing import Dict


def parse_colours_and_quantities(game_run) -> Dict[str, int]:
    # Parse the different colours and their quantities out
    cur_game_colours = game_run.split(", ")
    # Put the colours into a dictionary
    colours = {}
    for game_colour in cur_game_colours:
        quantity, colour = game_colour.split(" ")
        colours[colour] = int(quantity)
    return colours


def get_game_id_and_line(game):
    # Remove any extra whitespace from start/end
    game = game.strip()
    # Split out the game header and sub_games
    game_header, game_line = game.split(":")
    # Split out the game ID by splitting the game header, discarding the first value
    _, game_id = game_header.split(" ")

    return game_id, game_line

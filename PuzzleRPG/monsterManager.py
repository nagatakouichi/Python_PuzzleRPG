import config

def print_monster_name(monster):
    monster_name = monster['name']
    symbol = config.ELEMENT_SYMBOLS[monster['element']]
    color = config.ELEMENT_COLORS[monster['element']]
    print(f'\033[3{color}m{symbol}{monster_name}{symbol}\033[0m', end='')
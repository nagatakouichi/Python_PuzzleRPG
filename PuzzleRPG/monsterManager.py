import config

def print_monster_name(monster):
    monster_name = monster['name']
    symbol = config.ELEMENT_SYMBOLS[monster['element']]
    color = config.ELEMENT_COLORS[monster['element']]
    print(f'\033[3{color}m{symbol}{monster_name}{symbol}\033[0m', end='')

def print_monster_element_boost(monster):
    element_boost = config.ELEMENT_BOOST[monster['element']]
    weekness = ''
    resist = ''
    for element, ratio in element_boost.items() :
        if ratio == 2.0 :
            resist = element
        elif ratio == 0.5 :
            weekness = element        

    weekness_symbol = config.ELEMENT_SYMBOLS[weekness]
    weekness_color = config.ELEMENT_COLORS[weekness]
    resist_symbol = config.ELEMENT_SYMBOLS[resist]
    resist_color = config.ELEMENT_COLORS[resist]
    
    print(f'{"弱点"} ', end='')
    print(f'\033[3{weekness_color}m{weekness_symbol}{weekness}{weekness_symbol}\033[0m ', end='')

    print(f'{"  抵抗"} ', end='')
    print(f'\033[3{resist_color}m{resist_symbol}{resist}{resist_symbol}\033[0m ', end='')
    print('')
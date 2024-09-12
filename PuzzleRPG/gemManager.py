import random
import config
import attackManager

def fill_gems():
    gems_slot = list()
    for num in range(14) :
        gems_slot.append(random.randint(0, 4))
    return gems_slot

def print_gems(gems_slot, is_print_alphabet = True):
    if is_print_alphabet :
        for alphabet in config.SLOT_ALPHABET_LIST :
            print(f'{alphabet} ', end='')
        print('')
        
    for gem in gems_slot :
        symbol = config.ELEMENT_SYMBOLS[config.ELEMENT_LIST[gem]]
        color = config.ELEMENT_COLORS[config.ELEMENT_LIST[gem]]
        print(f'\033[3{color}m{symbol} \033[0m', end='')
    print('')

def check_valid_command(command):
    if len(command) != 2 :
        return False
    command_first, command_second = command[:1], command[1:]
    if command_first == command_second :
        return False
    if (command_first in config.SLOT_ALPHABET_LIST) and (command_second in config.SLOT_ALPHABET_LIST) :
        return True
    else:
        return False

def move_gem_command(gems_slot, command, is_print = True):
    command_first, command_second = command[:1], command[1:]
    first_index = config.SLOT_ALPHABET_LIST.index(command_first)
    second_index = config.SLOT_ALPHABET_LIST.index(command_second)
    move_gem(gems_slot, first_index, second_index, is_print)

def move_gem(gems_slot, first_index, second_index, is_print = True):
    if first_index < second_index :
        for i in range(second_index - first_index) :
            swap_gem(gems_slot, first_index + i, False)
            if is_print :
                print_gems(gems_slot, False)
                print('')
    else:
        for i in range(first_index - second_index) :
            swap_gem(gems_slot, first_index - i, True)
            if is_print :
                print_gems(gems_slot, False)
                print('')

def swap_gem(gems_slot, swap_gem_index, is_swap_left):
    destination_index = 0
    if is_swap_left :
        destination_index = swap_gem_index - 1
    else:
        destination_index = swap_gem_index + 1
    destination_element = gems_slot[destination_index]
    gems_slot[destination_index] = gems_slot[swap_gem_index]
    gems_slot[swap_gem_index] = destination_element

def evaluate_gems(gems_slot, monster, party):
    is_combo = True
    combo_num = 0
    while is_combo :
        while True :
            banishable_slot = check_banishable(gems_slot)
            if len(banishable_slot) <= 0 :
                break
            combo_num += 1
            banish_gems(gems_slot, banishable_slot, monster, party, combo_num)
            shift_gems(gems_slot, banishable_slot)
        spawn_gems(gems_slot)
        banishable_slot = check_banishable(gems_slot)
        if len(banishable_slot) <= 0 :
            is_combo = False

def check_banishable(gems_slot):
    slot_num = 0
    consecutive_gems = list()

    for gem in gems_slot :
        if len(consecutive_gems) <= 0 :
            consecutive_gems.append(gem)
        else:
            if gem == consecutive_gems[0] :
                consecutive_gems.append(gem)
            else:
                if len(consecutive_gems) >= 3 :
                    break
                else:
                    consecutive_gems = list()
                    consecutive_gems.append(gem)
        slot_num += 1

    banishable_slot = list()
    if len(consecutive_gems) >= 3 and consecutive_gems[0] != 5 :
        banishable_slot = range(slot_num - len(consecutive_gems), slot_num)
    return banishable_slot

def banish_gems(gems_slot, banishable_slot, monster, party, combo_num) :
    banish_num = len(banishable_slot)
    if banish_num > 0 :
        element = gems_slot[banishable_slot[0]]
        for slot in banishable_slot :
            gems_slot[slot] = 5
        print_gems(gems_slot, False)
        if combo_num >= 2 :
            print(f'{combo_num}COMBO!')
        if element == 4 :
            attackManager.do_recover(party, combo_num, banish_num)
        else:
            attackManager.do_attack(monster, party, element, combo_num, banish_num)

def shift_gems(gems_slot, banishable_slot):
    print_gems(gems_slot, False)
    for banish_slot in reversed(banishable_slot) :
        move_gem(gems_slot, banish_slot, len(gems_slot) - 1, False)
        print_gems(gems_slot, False)

def spawn_gems(gems_slot):
    is_spawn = False
    for num in range(len(gems_slot)) :
        if gems_slot[num] == 5 :
            gems_slot[num] = random.randint(0, 4)
            is_spawn = True
    if is_spawn :
        print_gems(gems_slot, False)
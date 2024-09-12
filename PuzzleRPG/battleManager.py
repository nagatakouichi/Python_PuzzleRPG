import monsterManager
import attackManager
import gemManager

def do_battle(monster_data, party):
    monsterManager.print_monster_name(monster_data)
    print('が現れた！\n')
    gems_slot = gemManager.fill_gems()
    is_win = 1
    is_battle = True
    is_player_turn = True
    while is_battle :
        print('')
        if is_player_turn:
            on_player_turn(party, monster_data, gems_slot)
            is_player_turn = False
        else:
            on_enemy_turn(party, monster_data)
            is_player_turn = True
            
        if party['hp'] <= 0:
            print('パーティのHPが0になった')
            is_win = 0
            is_battle = False
        elif monster_data['hp'] <= 0:
            monsterManager.print_monster_name(monster_data)
            print('を倒した！')
            is_battle = False    
    
    return is_win

def on_player_turn(party, monster, gems_slot):
    print(f'【{party['player_name']}のターン】(HP={party['hp']})')
    show_battle_field(party, monster, gems_slot)
    
    command = ''
    is_correct_command = False
    while not is_correct_command :
        command = input('コマンド？ >')
        is_correct_command = gemManager.check_valid_command(command)
        if not is_correct_command :
            print('エラー:コマンドが正しくありません。 もう一度入力してください。')
    gemManager.move_gem_command(gems_slot, command)
    gemManager.evaluate_gems(gems_slot, monster, party)

def on_enemy_turn(party, monster):
    print('【', end='')
    monsterManager.print_monster_name(monster)
    print(f'のターン】(HP={monster['hp']})')
    attackManager.do_enemy_attack(monster, party)

def show_battle_field(party, monster, gems_slot):
    monsterManager.print_monster_name(monster)
    print(f'HP = {monster['hp']} / {monster['max_hp']}\n')
    monsterManager.print_monster_element_boost(monster)
    for friend in party['friends'] :
        monsterManager.print_monster_name(friend)
        print(' ', end='')
    print(f'\nHP = {party['hp']} / {party['max_hp']}')
    print('------------------------------')
    gemManager.print_gems(gems_slot)
    print('------------------------------')
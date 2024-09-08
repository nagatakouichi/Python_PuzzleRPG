#import
import partyManager
import battleManager

#function
def main():
    player_name = ''
    while player_name == '':
        player_name = input('プレイヤー名を入力してください> ')
        if player_name == '':
            print('エラー：プレイヤー名を入力してください')
            
    print('*** Puzzule Battle ***')

    slime = {'name':'スライム', 'hp':100, 'max_hp':100, 'element':'水', 'ap':10, 'dp':1}
    goblin = {'name':'ゴブリン', 'hp':200, 'max_hp':200, 'element':'土', 'ap':20, 'dp':5}
    giantbat = {'name':'オオコウモリ', 'hp':300, 'max_hp':300, 'element':'風', 'ap':30, 'dp':10}
    werewolf = {'name':'ウェアウルフ', 'hp':400, 'max_hp':400, 'element':'風', 'ap':40, 'dp':15}
    dragon = {'name':'ドラゴン', 'hp':600, 'max_hp':600, 'element':'火', 'ap':50, 'dp':20}
    monsters = [slime, goblin, giantbat, werewolf, dragon]
    
    seiryu = {'name':'青龍', 'hp':150, 'max_hp':150, 'element':'風', 'ap':15, 'dp':10}
    suzaku = {'name':'朱雀', 'hp':150, 'max_hp':150, 'element':'火', 'ap':25, 'dp':10}
    byakko = {'name':'白虎', 'hp':150, 'max_hp':150, 'element':'土', 'ap':20, 'dp':5}
    genbu = {'name':'玄武', 'hp':150, 'max_hp':150, 'element':'水', 'ap':20, 'dp':15}
    friends = [seiryu, suzaku, byakko, genbu]
    party = partyManager.organize_party(player_name, friends)
    
    beat_monster_num = go_dungion(player_name, monsters, party)
    if beat_monster_num < 5:
        print('*** GAME OVER ***')
    else:
        print('*** GAME CLEAR!! ***')
    print(f'倒したモンスターの数={beat_monster_num}')

def go_dungion(player_name, monsters, party):
    print(f'{player_name}のパーティ(HP={party['hp']})はダンジョンに到着した')
    partyManager.show_party(party)
    win_num = 0
    for monster_data in monsters:
        is_win = battleManager.do_battle(monster_data, party)
        win_num += is_win
        if party['hp'] <= 0 :
            print(f'{player_name}はダンジョンから逃げ出した')
            break
        else :
            print(f'{player_name}はさらに奥へと進んだ')
            print('==============================')

    if party['hp'] > 0 :
        print(f'{player_name}はダンジョンを制覇した')
    return win_num

#main
main()
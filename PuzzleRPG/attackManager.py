import random
import math
import config
import monsterManager

def do_attack(monster, party, element, combo_num, banish_num):
    damage = 0
    attack_friend = None
    for friend in party['friends'] :
        if friend['element'] == config.ELEMENT_LIST[element] :
            attack_friend = friend

    if attack_friend == None :
        print('攻撃エラー')
        return

    damage = attack_friend['ap'] - monster['dp']
    damage = damage * config.ELEMENT_BOOST[attack_friend['element']][monster['element']]
    damage = blur_damage(damage, -0.1, 0.1)
    damage = damage * (1.5 ** (banish_num - 3 + combo_num))    #コンボ補正
    damage = int(damage)
    if damage <= 0 :
        damage = 1
    monster['hp'] -= damage

    monsterManager.print_monster_name(attack_friend)
    print('の攻撃！')
    print(f'{monster['name']}に{damage}のダメージを与えた')

def do_enemy_attack(monster, party):
    damage = monster['ap'] - party['dp']
    damage = blur_damage(damage, -0.1, 0.1)
    damage = int(damage)
    if damage <= 0 :
        damage = 1
    party['hp'] -= damage
    print(f'パーティは{damage}のダメージを受けた')

def do_recover(party, combo_num, banish_num):
    heal = 20
    heal = heal * (1.5 ** (banish_num - 3 + combo_num)) #コンボ補正
    heal = blur_damage(heal, -0.1, 0.1)
    heal = int(heal)
    if party['hp'] + heal > party['max_hp'] :
        heal = party['max_hp'] - party['hp']
    party['hp'] += heal
    print(f'パーティは{heal}回復した')
    print(f'パーティのHP {party['hp']}/{party['max_hp']}')

def blur_damage(damage, lower_limit_ratio, higher_limit_ratio):
    rand = random.uniform(lower_limit_ratio, higher_limit_ratio)
    damage =  math.floor(damage * (1 + rand))
    return damage
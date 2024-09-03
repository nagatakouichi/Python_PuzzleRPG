import monsterManager

def organize_party(player_name, friends):
    max_hp = 0
    dp_sum = 0
    for friend_data in friends:
        max_hp += friend_data['hp']
        dp_sum += friend_data['dp']
    dp = dp_sum / len(friends)
    party = {'player_name':player_name, 'friends':friends, 'hp':max_hp, 'max_hp':max_hp, 'dp':dp}
    return party

def show_party(party):
    print('＜パーティ編成＞----------------')
    for friend_data in party['friends']:
        monsterManager.print_monster_name(friend_data)
        print(f' HP= {friend_data['hp']} 攻撃= {friend_data['ap']} 防御= {friend_data['dp']}')
        
    print('------------------------------\n')
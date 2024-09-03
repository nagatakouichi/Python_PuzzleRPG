#global variables
ELEMENT_LIST = ['火', '水', '風', '土', '命', '無']
ELEMENT_SYMBOLS = {'火':'$', '水':'~', '風':'@', '土':'#', '命':'&', '無':' '}
ELEMENT_COLORS = {'火':1, '水':6, '風':2, '土':3, '命':5, '無':7}
FIRE_BOOST = {'火':1.0, '水':0.5, '風':2.0, '土':1.0, '命':1.0, '無':1.0}
WATER_BOOST = {'火':2.0, '水':1.0, '風':1.0, '土':0.5, '命':1.0, '無':1.0}
WIND_BOOST = {'火':0.5, '水':1.0, '風':1.0, '土':2.0, '命':1.0, '無':1.0}
DIRT_BOOST = {'火':1.0, '水':2.0, '風':0.5, '土':1.0, '命':1.0, '無':1.0}
NO_BOOST = {'火':1.0, '水':1.0, '風':1.0, '土':1.0, '命':1.0, '無':1.0}
ELEMENT_BOOST = {'火':FIRE_BOOST, '水':WATER_BOOST, '風':WIND_BOOST, '土':DIRT_BOOST, '命':NO_BOOST, '無':NO_BOOST}
SLOT_ALPHABET_LIST = list('ABCDEFGHIJKLMN')
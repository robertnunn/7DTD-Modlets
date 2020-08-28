import os
from pprint import pprint as pp
from bs4 import BeautifulSoup as BS
import re

alpha_num = 19

base_path = f'D:/Games/7DTD/7DTD-Modlets/Alpha {str(alpha_num)}/A{str(alpha_num)}-Config/'
sound_path = base_path + 'sounds.xml'
block_path = base_path + 'blocks.xml'
sound_dict = dict()
block_dict = dict()

with open(sound_path, 'r') as s:
    sounds_raw = s.read()
with open(block_path, 'r') as b:
    blocks_raw = b.read()
sound_soup = BS(sounds_raw, 'lxml')
block_soup = BS(blocks_raw, 'lxml')
heat_re = re.compile('heat', re.IGNORECASE)

# print(len(sound_soup))
# print(len(block_soup))

def find_heat(tag):
    return tag.has_attr('heat_map_strength') or tag.get('name') == 'HeatMapStrength'

sounds = sound_soup.find_all(find_heat)
blocks = block_soup.find_all(find_heat)
block_list = list()

# pp(len(sounds))
# pp(len(blocks))
# pp(blocks)

for i in sounds:
    sound_dict[i.parent.get('name')] = {'str': i.get('heat_map_strength'), 'time': i.get('heat_map_time')}

for i in blocks:
    block_list.append(i.parent)

# pp(block_list)

for i in block_list:
    block_dict[i.get('name')] = {'str': i.find('property', attrs={'name': 'HeatMapStrength'}).get('value'), 'time': i.find('property', attrs={'name': 'HeatMapTime'}).get('value')}

pp(sound_dict)
pp(block_dict)

csv_list = ['Type,Name,Strength,Time,Frequency']
for k,v in sound_dict.items():
    csv_list.append(f'Sound,{k},{v.get("str")},{v.get("time")},{v.get("freq", "")}')

for k,v in block_dict.items():
    csv_list.append(f'Block,{k},{v.get("str")},{v.get("time")},{v.get("freq", "")}')

csv = '\n'.join(csv_list)

with open(base_path + '../../Python Scripts/heat map values.csv', 'w') as c:
    c.write(csv)
import xml.etree.ElementTree as et
import os
from pprint import pprint as pp

os.chdir("D:/Games/7DTD/7DTD-Modlets/Alpha 18/ignore")
path = "D:/Games/7DTD/7DTD-Modlets/Alpha 18/A18-Config/"
filename = 'sounds.xml'
blank_animal = 'invisibleAnimal'
blank_enemy = 'invisibleAnimalEnemy'

tree = et.parse(path+filename)
nodes = tree.findall('./SoundDataNode')
fire_list = list()
heat_dict = dict()
mod_list = list()

for i in nodes:
    name = i.get('name')
    if name.endswith('_fire'):
        noise = i.findall('./Noise')
        # print(noise)
        for j in noise:
            heat_dict[name] = [j.get('heat_map_strength'), j.get('heat_map_time')]

for i in heat_dict:
    if heat_dict[i][0] != None:
        mod_list.append(f'<set xpath="/Sounds/SoundDataNode[@name=\'{i}\']/noise/@heat_map_strength">{str(round(float(heat_dict[i][0])*2, 2))}</set>')
    

pp(mod_list)
# pp(fire_list)
# pp(heat_dict)
with open('heat map bump.xml', mode='w') as heat:
    heat.write('\n'.join(mod_list))
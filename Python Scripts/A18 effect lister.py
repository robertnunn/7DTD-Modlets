import xml.etree.ElementTree as et
import os
from pprint import pprint as pp

path = "D:/Games/7DTD/7DTD-Modlets/Alpha 18/A18-Config/"
filenames = {'progression.xml': './perk/perks', 'item_modifiers.xml': './item_modifier'}

def get_effects(path, filename, find_string):
    path += filename
    print(path)
    tree = et.parse(path)
    effect_set = set()

    nodes = tree.findall("./perks/perk")
    for node in nodes:
        name = node.get('name')
        print(name)
        effects = node.findall('./effect_group/passive_effect')
        for eff in effects:
            effect_set.add(eff.get('name'))
    
    return effect_set

master_set = set()
for i in filenames:
    temp_set = get_effects(path, i, filenames[i])
    master_set = master_set.union(temp_set)

print(master_set)

mod_effect_list = '\n'.join(sorted(list(master_set)))
with open('effect list.txt', mode='w') as csv_file:
    csv_file.write(mod_effect_list)
# pp(hp_list)

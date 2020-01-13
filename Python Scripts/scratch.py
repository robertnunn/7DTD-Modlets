import xml.etree.ElementTree as et
import os
from pprint import pprint as pp

path = "D:/Games/7DTD/7DTD-Modlets/Alpha 18/A18-Config/"
filename = 'entitygroups.xml'
blank_animal = 'invisibleAnimal'
blank_enemy = 'invisibleAnimalEnemy'

groups_tree = et.parse(path+filename)
groups = groups_tree.findall('./entitygroup/entity')
full_entity_set = set()
zombie_set = set()
non_zombie_set = set()

for i in groups:
    name = i.get('name')
    full_entity_set.add(name)
    if 'zombie' not in name.lower():
        non_zombie_set.add(name)
    else:
        zombie_set.add(name)

# pp(entity_set)
pp(non_zombie_set)
pp(zombie_set)
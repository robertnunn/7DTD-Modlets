import xml.etree.ElementTree as et
import os

loot_xml = 'D:/Games/7DTD/7DTD-Modlets/Alpha 18/A18-Config/loot.xml'
loot_file = et.parse(loot_xml)
loot_nodes = loot_file.findall('./lootgroup')
groups = []

for group in loot_nodes:
    groups.append(group.get('name'))
    print(group.get('name'))
# print(groups)
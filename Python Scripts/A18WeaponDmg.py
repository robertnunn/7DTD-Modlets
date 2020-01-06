import os
import xml.etree.ElementTree as et
import logging
import math
"""
    for Python v3.6+
    This lets you modify the weapon damage for all player weapons as a batch.
    You have to option to add a flat amount and/or multiply weapon damage
    The True/False values are case sensitive in python
"""
logging.basicConfig(level=logging.DEBUG, filename='A18WeaponDmg.log', filemode='w')
path = os.path.dirname(__file__)  # gets the absolute path to this file, minus the filename
# path = r'A18/'  # set this to an empty string to search in the same folder
filename = '/../A18-Config/items.xml'
dmg_mult = 2  # (float) multiply all player damage by this value, rounding fractions up. 1 = no change
dmg_add = 20  # (int) add this to all player damage
DO_MULT = True  # (True/False) do we multiply weapon damage?
DO_ADD = False  # (True/False) do we add to weapon damage?

os.chdir(path)
path += filename
tree = et.parse(path)
items = tree.findall('./item')
results = ['<?xml version="1.0" encoding="UTF-8"?>\n<configs>']
logging.debug(type(items))


def make_change(damage):
    damage = float(damage)
    if DO_ADD:
        damage += dmg_add
    if DO_MULT:
        damage = math.ceil(damage * dmg_mult)
    return damage


for item in items:
    name = item.get('name')
    if name.lower().find('zombie') != -1:
        logging.debug("ZOMBIE FOUND: " + name)
    else:
        # logging.debug("item is: " + item.get('name'))
        elems = item.findall('./effect_group[@name="' + name + '"]/passive_effect[@name="EntityDamage"][@operation="base_set"]')
        logging.debug(str(len(elems)))
        for i in elems:
            dmg = i.get('value')
            new_dmg = make_change(dmg)
            # i.set('value', str(new_dmg))
            logging.info("Weapon is: " + item.get('name'))
            logging.info("Changing: " + str(dmg) + " to: " + str(new_dmg))
            results.append('\t<set xpath="/items/item[@name=\'' + name + '\']/effect_group[@name=\'' + name + '\']/passive_effect[@name=\'EntityDamage\'][@operation=\'base_set\']/@value">' + str(new_dmg) + '</set> <!-- default: ' + str(dmg) + ' -->')

results.append('</configs>')
with open('weap_xpath.xml', mode='w') as xml_out:
    xml_out.write('\n'.join(results))
# tree.write('output.xml', encoding='utf-8')

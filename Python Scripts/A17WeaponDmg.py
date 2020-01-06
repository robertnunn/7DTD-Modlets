import os
import xml.etree.ElementTree as et
import logging
import math
"""
    for Python v3.6+
    This lets you modify the weapon damage for all player weapons as a batch.
    You have to option to add a flat amount and/or multiply weapon damage
    The True/False values are case sensitive in python
    Obsolete as of alpha 17!
"""
logging.basicConfig(level=logging.INFO, filename='A17WeaponDmg.log', filemode='w')
path = 'D:\\Programming\\Python\\7DTD\\A17\\'  # set this to an empty string to search in the same folder
filename = 'items.xml'
dmg_mult = 5  # (float) multiply all player damage by this value, rounding fractions up. 1 = no change
dmg_add = 20  # (int) add this to all player damage
DO_MULT = True  # (True/False) do we multiply weapon damage?
DO_ADD = False  # (True/False) do we add to weapon damage?

os.chdir(path)
path += filename
tree = et.parse(path)
items = tree.findall('./item')
results = []
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
        elems = item.findall('./effect_group[@name="Base Effects"]/passive_effect[@name="EntityDamage"][@operation="base_set"]')
        logging.debug(str(len(elems)))
        for i in elems:
            dmg = i.get('value')
            new_dmg = make_change(dmg)
            # i.set('value', str(new_dmg))
            logging.info("Weapon is: " + item.get('name'))
            logging.info("Changing: " + str(dmg) + " to: " + str(new_dmg))
            results.append('<set xpath="/items/item[@name=\'' + name + '\']/effect_group[@name=\'Base Effects\']/passive_effect[@name=\'EntityDamage\'][@operation=\'base_set\']/@value">' + str(new_dmg) + '</set>')

with open('weap_xpath.xml', mode='w') as xml_out:
    xml_out.write('\n'.join(results))
# tree.write('output.xml', encoding='utf-8')

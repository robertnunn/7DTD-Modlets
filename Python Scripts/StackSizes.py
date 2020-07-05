import os
import xml.etree.ElementTree as et
import logging
import math
import bs4
"""
    for Python v3.6+
    This lets you modify the weapon damage for all player weapons as a batch.
    You have to option to add a flat amount and/or multiply weapon damage
    The True/False values are case sensitive in python
    Obsolete as of alpha 17!
"""
logging.basicConfig(level=logging.DEBUG, filename='A19StackSizes.log', filemode='w')
path = os.path.dirname(__file__)  # gets the absolute path to this file, minus the filename

filename = '/../Alpha 19/A19-Config/items.xml'  # leading / is needed because the absolute path above doesn't include one at the end of the string
val_mult = 3  # (float) multiply all player value by this value, rounding fractions up. 1 = no change
val_add = 20  # (int) add this to all player value
DO_MULT = True  # (True/False) do we multiply the value?
DO_ADD = False  # (True/False) do we add to the value?

os.chdir(path)
path += filename
tree = et.parse(path)
items = tree.findall('./item')
results = ['<?xml version="1.0" encoding="UTF-8"?>\n<configs>']
logging.debug(type(items))


def make_change(value):
    value = float(value)
    if DO_ADD:
        value += val_add
    if DO_MULT:
        value = math.ceil(value * val_mult)
    if value > 32768:
        value = 32000
        logging.info("ERROR: New value above signed integer max (32768), defaulting to 32000. Stack sizes above 32768 have been known to cause a total character reset (including to original spawn point) when using stack sizes larger than this. If you wish to have a larger value, you must manually enter it.")
    return value


for item in items:
    name = item.get('name')
    if name.lower().find('ammo') != -1:  # if we DO find the search term(s), do this
        i = item.find('./property[@name=\'Stacknumber\']')
        if i != None:  # if this item has a Stacknumber property
            val = i.get('value')
            new_val = make_change(val)
            results.append('\t<set xpath="/items/item[@name=\'' + name + '\']/property[@name=\'Stacknumber\']/@value">' + str(new_val) + '</set>  <!-- default: ' + val + ' -->')
    else:  # if we DON'T find the thing we're looking for
        logging.debug("Item: " + name + "didn't have a stack number property")

results.append('</configs>')
with open('ammo_xpath.xml', mode='w') as xml_out:
    xml_out.write('\n'.join(results))
import xml.etree.ElementTree as et
import os
from pprint import pprint as pp

# prints a list of base resources in the items file specified by items_xml
items_xml = 'D:/Games/7DTD/7DTD-Modlets/Alpha 19/A19-Config/items.xml'
items_file = et.parse(items_xml)
item_nodes = items_file.findall('./item')
resources = []

for item in item_nodes:
    if item.get('name').startswith('resource'):
        resources.append(item.get('name'))

pp(resources)
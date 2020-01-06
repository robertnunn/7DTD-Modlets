import os
import xml.dom.minidom as md
from pprint import pprint as pp
import itertools

path = 'D:\\Programming\\Python\\7DTD\\War of the Walkers\\'
filename = 'items.xml'

os.chdir(path)
# print(os.getcwd())
path += filename
# print(pp(os.listdir(path)))
tree = md.parse(path)
items = tree.getElementsByTagName('item')
results = dict()
search_list = ['Gain_food',
               'Gain_water',
               'Gain_stamina',
               'Gain_health',
               'Gain_wellness',
               'Buff',
               'Debuff',]


def pull_data(elems, search_list):
    properties = make_empty_stats(search_list)
    for prop in elems:
        name = prop.getAttribute('name')
        if name in search_list:
            properties[name] = prop.getAttribute('value')

    return properties


def make_empty_stats(search_list):
    p = dict()
    for i in search_list:
        p[i] = ''
    return p


for item in items:
    name = item.getAttribute('name')
    # props = item.childNodes
    for prop in item.childNodes:
        if prop.nodeType == 1:
            if prop.getAttribute('class') == "Action1":
                elems = prop.getElementsByTagName('property')
                consumable = False
                for i in elems:
                    if i.getAttribute('name') == 'Class' and i.getAttribute('value') == "Eat":
                        consumable = True
                if consumable:
                    results[name] = pull_data(elems, search_list)

# pp(results.keys())
csv_list = [','.join(['item name', 'food', 'water', 'health', 'stamina', 'wellness', 'Buff', 'Debuff'])]
for item in results.keys():
    entry = [item,
            results[item]['Gain_food'],
            results[item]['Gain_water'],
            results[item]['Gain_health'],
            results[item]['Gain_stamina'],
            results[item]['Gain_wellness'],
            results[item]['Buff'].replace(',', ';'),
            results[item]['Debuff'].replace(',', ';')]
    entry = ','.join(entry)
    csv_list.append(entry)

# pp(csv_list)
# csv_list = itertools.chain.from_iterable(csv_list)
csv = '\n'.join(csv_list)
# with open('consumables.csv', 'w') as c:
#     c.write(csv)

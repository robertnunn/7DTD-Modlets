import os
from pprint import pprint as pp
from bs4 import BeautifulSoup as BS
import re

alpha_num = 19
base_path = f'D:/Games/7DTD/7DTD-Modlets/Alpha {str(alpha_num)}/A{str(alpha_num)}-Config/'

with open(base_path + 'materials.xml') as m:
    soup_materials = BS(m.read(), 'lxml')

with open(base_path + 'items.xml') as i:
    soup_items = BS(i.read(), 'lxml')

mat_tags = soup_materials.find_all('material')
mat_dict = dict()

# a = soup_materials.find('material', id='Morganic')
# b = a.find('property', attrs={'name': 'forge_category'})
# print(b)

for tag in mat_tags:
    # print(tag)
    # print(tag.get('id'))
    mat = tag.find('property', attrs={'name': 'forge_category'})
    if mat == None:
        mat_dict[tag.get('id')] = 'Not Scrappable'
    else:
        mat_dict[tag.get('id')] = mat.get('value')

item_scrap_list = ['Item,Scraps to']
items = soup_items.find_all('item')
for tag in items:
    mat = tag.find('property', attrs={'name': 'Material'})
    if mat == None:
        item_scrap_list.append(f"{tag.get('name')},Not Scrappable")
    else:
        item_scrap_list.append(f"{tag.get('name')},{mat_dict[mat.get('value')]}")
    

with open('scrap.csv', mode='w') as s:
    s.write('\n'.join(item_scrap_list))
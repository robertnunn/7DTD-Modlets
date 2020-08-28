import os
from pprint import pprint as pp
from bs4 import BeautifulSoup as BS
import re

alpha_num = 19

base_path = f'D:/Games/7DTD/7DTD-Modlets/Alpha {str(alpha_num)}/A{str(alpha_num)}-Config/'
gs_re = re.compile(r'[a-zA-Z]*(\d{1,4})$')

with open(base_path + 'entitygroups.xml', 'r') as e:
    entity_raw = e.read()
soup = BS(entity_raw, 'lxml')

entity_set = set()
entities = soup.find_all('entity')
for i in entities:
    entity_set.add(i.get('name'))

# pp(entity_set)

zombie = 'zombieSpiderFeral'
z_set = soup.find_all('entity', attrs={'name': zombie})
groups = [i.parent.get('name') for i in z_set]
# pp(groups)
group_nums = list()
group_no_num = list()
for i in groups:
    if gs_re.search(i) != None:
        group_nums.append(int(gs_re.search(i).groups(1)[0]))
    else:
        group_no_num.append(i)
# pp(group_nums)
group_nums.sort()
print(group_nums[0])
pp(group_no_num)

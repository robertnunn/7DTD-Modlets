import xml.etree.ElementTree as et
import os
from pprint import pprint as pp

os.chdir("D:/Games/7DTD/7DTD-Modlets/Alpha 18/ignore")
path = "D:/Games/7DTD/7DTD-Modlets/Alpha 18/A18-Config/"
filename = 'spawning.xml'
blank_animal = 'invisibleAnimal'
blank_enemy = 'invisibleAnimalEnemy'

tree = et.parse(path+filename)
nodes = tree.findall('./biome')
names = list()

for i in nodes:
    names.append(i.get('name'))

pp(names)
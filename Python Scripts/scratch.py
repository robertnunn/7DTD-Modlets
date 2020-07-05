import xml.etree.ElementTree as et
import os
from pprint import pprint as pp

os.chdir("D:/Games/7DTD/7DTD-Modlets/Alpha 19")
path = "D:/Games/7DTD/7DTD-Modlets/Alpha 19/A19-Config/"

dir_scan = os.scandir()
dir_list = list()

for i in dir_scan:
    dir_list.append(i.name)

for i in dir_list:
    os.rename(i, i[6:])
pp(dir_list)
import os
import xml.etree.ElementTree as et
import logging
import math

alpha_num = 19
log_file_name = f'A{str(alpha_num)} better silencers.log'

logging.basicConfig(level=logging.DEBUG, filename=log_file_name, filemode='w')
path = os.path.dirname(__file__)  # gets the absolute path to this file, minus the filename

filename = f'/../Alpha {str(alpha_num)}/A{str(alpha_num)}-Config/sounds.xml'  # leading / is needed because the absolute path above doesn't include one at the end of the string

reduction_factor = 3

os.chdir(path)
path += filename
tree = et.parse(path)
noises = tree.findall('./SoundDataNode')
xml = list()
xml.append('<?xml version="1.0" encoding="UTF-8"?>\n<configs>\n')

for node in noises:
    if node.get('name').endswith('_s_fire'):
        noise_level = node.find('./Noise').get('noise')
        new_level = int(noise_level) // reduction_factor
        xml.append(f'\t<set xpath="/Sounds/SoundDataNode[@name=\'{node.get("name")}\']/Noise/@noise">{str(new_level)}</set>  <!-- default: {noise_level}-->\n')

xml.append('</configs>')

with open('bettersilencers.xml', mode='w') as s:
    s.write(''.join(xml))
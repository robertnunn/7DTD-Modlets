"""
    This script is for python 3.6+, and is intended to take a list of items
    and output a list of containers that could spawn it, as well as a percentage
    chance of getting the item in a given container
"""
import os
import xml.etree.ElementTree as et
import logging
import sqlalchemy as sa
import sqlite3 as sl

logging.basicConfig(level=logging.DEBUG, filename='loot finder.log', filemode='w')
path = 'D:\\Programming\\Python\\7DTD\\A17\\'  # set this to an empty string to search in the same folder
filenames = ['items.xml', 'loot.xml', 'blocks.xml']
items_to_find = ['modGunSoundSuppressorSilencerSchematic',
                 'modGunSoundSuppressorSilencer',
                 'modGunScopeLarge',
                 'modGunScopeLargeSchematic',
                 'modGunMagazineExtender',
                 'modGunMagazineExtenderSchematic',
                 ]
logging.debug('path is: ' + path)
# loot.xml has both lootgroup and lootcontainer
os.chdir(path)
path += filenames[1]
tree = et.parse(path)
lgs = tree.findall('./lootgroup')
logging.debug(type(lgs))
logging.debug(len(lgs))

data = {'lgs': dict(), 'cnt': dict()}

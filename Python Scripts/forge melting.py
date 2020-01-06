import xml.etree.ElementTree as et
import os
import itertools
from pprint import pprint as pp

items_xml = 'D:/Games/7DTD/7DTD-Modlets/Alpha 18/A18-Config/items.xml'
items_file = et.parse(items_xml)
item_nodes = items_file.findall('./item')
# forge_mats = {'stone': [], 'iron': [], 'sand': [], 'brass': [], 'clay': [], 'lead': []}
forge_mats = dict()
stone = 'stone'
iron = 'iron'
sand = 'sand'
brass = 'brass'
clay = 'clay'
lead = 'lead'
mats_blank = {stone: [], iron: [], sand: [], brass: [], clay: [], lead: []}
likely_mats = mats_blank
# these six lists were made by guessing which material types would give which forge mat
mstone = ['Mstone', 'MresourceCobblestones', 'MresourceCement', 'MresourceConcreteMix', 'MresourceRockSmall']
miron = ['Mmetal', 'MmechanicalParts', 'MmeleeToolAllSteel', 'MMotorToolParts', 'MmeleeToolKnifeMachete', 'MmeleeStunBatonParts', 'MmeleeThrownSpearSteel', 'MmeleeToolSledgehammerSteel', 'MmeleeKnucklesSteelParts', 'MelectricParts', 'MHandGunParts', 'MShotgunParts', 'MRifleParts', 'MMachineGunParts', 'MRocketLauncherParts', 'MBowCrossbowParts', 'MJunkTurretParts', 'MFuelBarrelMetal', 'MarmorSteelSet', 'MresourceScrapIron', 'MresourceForgedIron', 'MresourceMetalPipe', 'MresourceForgedSteel', 'MelectronicParts', 'Msteel', 'MresourceHubcap', 'MsmallEngine', 'Miron']
msand = ['MresourceCrushedSand', 'MresourceBrokenGlass', 'Mglass', 'MtoolBeaker']
mbrass = ['MresourceScrapBrassSmall', 'Mbrass', 'MresourceScrapBrassMedium', 'MresourceScrapBrassLarge']
mlead = ['Mlead_scrap', 'MresourceScrapLeadSmall', 'MresourceScrapLeadMedium', 'MresourceScrapLeadLarge']
mclay = ['MresourceClayLump']

for item in item_nodes:
    name = item.get('name')
    try:
        material = item.find('./property[@name="Material"]').get('value')
    except:
        material = 'None'

    try:
        forge_mats[material].append(name)
    except KeyError:
        forge_mats[material] = []
        forge_mats[material].append(name)

stone_mats = [j for j in itertools.chain.from_iterable([forge_mats[i] for i in mstone])]
iron_mats = [j for j in itertools.chain.from_iterable([forge_mats[i] for i in miron])]
sand_mats = [j for j in itertools.chain.from_iterable([forge_mats[i] for i in msand])]
brass_mats = [j for j in itertools.chain.from_iterable([forge_mats[i] for i in mbrass])]
lead_mats = [j for j in itertools.chain.from_iterable([forge_mats[i] for i in mlead])]
clay_mats = [j for j in itertools.chain.from_iterable([forge_mats[i] for i in mclay])]

likely_mats = {stone: stone_mats, iron: iron_mats, sand: sand_mats, brass: brass_mats, lead: lead_mats, clay: clay_mats}

pp(likely_mats)
# brass_stuff = [forge_mats[i] for i in brass_mats]
# stone_mats
# print([forge_mats[i] for i in mstone])
# res_list = [i for i in stone_mats]

# print(brass_stuff)
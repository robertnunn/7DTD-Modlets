import xml.etree.ElementTree as et
import os

v_num = 19

def find_schematic(item, schem_unlock_dict):  # finds the schematic that unlocks a given item, can be told to specifically look in certain schematics
    # for i in start_schematics:
    #     if item in schem_unlock_dict[i]:
    #         return i
    for i in schem_unlock_dict:
        if item in schem_unlock_dict[i]:
            return i
    return None


items_xml = f'D:/Games/7DTD/7DTD-Modlets/Alpha {str(v_num)}/A{str(v_num)}-Config/items.xml'
prog_xml = f'D:/Games/7DTD/7DTD-Modlets/Alpha {str(v_num)}/A{str(v_num)}-Config/progression.xml'
# these exceptions are done by hand and come from deviations from the pattern of using "{item_name}Schematic" for the schematic and "{item_name}" for the icon
exceptions =    {   'resourceGunPowderBundle': 'resourceGunPowder',
                    'mineCookingPot': 'toolCookingPot',
                    'rScrapIronPlateMine': 'rScrapIronPlate',
                    'ammoGasCanBundle': 'ammoGasCan',
                }
# the fun pimps seem to have left some deprecated items in their xmls, so we have to work around them
deprecated_items = ['medicalBloodDrawKitSchematic']
items_file = et.parse(items_xml)
perk_file = et.parse(prog_xml)
item_nodes = items_file.findall('./item')
perk_nodes = perk_file.findall('./perks/perk')
schematics_set = set()
new_schematics_set = set()
schem_unlock_dict = dict()
prog_mods = list()
recipes = list()
items = list()
perk_recipes = list()

for item in item_nodes:  # 
    name = item.get('name')
    if name.endswith('Schematic') or name.startswith('book'):
        # print(name)
        if name not in deprecated_items:
            schematics_set.add(name)
            # next two lines build a schematic/book dictionary with the item name as a key, and the recipes it unlocks as a list of values
            unlocked = item.findall('./effect_group/triggered_effect[@action="ModifyCVar"]')
            schem_unlock_dict[name] = [i.get('cvar') for i in unlocked]
# print(schematics_set)
# print(schem_unlock_dict)

print('debug')  # hooray print debugging! what's "import logging"?
# print(perk_nodes)
for perk in perk_nodes:  # this loop does all the progression modification
    name = perk.get('name')
    if perk.get('base_skill_point_cost') == None:  # only proceeds on non-book perks
        recipe_unlocks = perk.findall('./effect_group/passive_effect[@name="RecipeTagUnlocked"]')
        if len(recipe_unlocks):
            print('-------------------------------------')
            print(name + ', ' + str(len(recipe_unlocks)))
            # print(recipe_unlocks)
            for i in recipe_unlocks:
                level = i.get('')
                tags = i.get('tags')  # get the recipes unlocked by this perk level
                tag_schematics = tags.split(',')
                valid_tag_schematics = set()
                invalid_tag_schematics = list()
                print(tag_schematics)
                for j in range(len(tag_schematics)):  # check if a schematic item already exists
                    name_schematic = f'{tag_schematics[j]}Schematic'
                    if name_schematic in schematics_set:
                        valid_tag_schematics.add(name_schematic)
                    else:
                        invalid_tag_schematics.append(tag_schematics[j])

                print('\tvalid:         ', valid_tag_schematics)
                print('\tinvalid:       ', invalid_tag_schematics)
                still_invalid = list()
                for k in invalid_tag_schematics:  # create recipes and schematic items for items that don't already have them 
                    schem = find_schematic(k, schem_unlock_dict)
                    if schem != None:  # if a schematic already exists, add it to the list for the current perk level
                        valid_tag_schematics.add(schem)
                    else:  # need to create a new schematic(item), recipe, prog append(add to valid_tag_schematics)
                        if k in exceptions.keys():
                            custom_icon = exceptions[k]
                        else:
                            custom_icon = k
                        valid_tag_schematics.add(k + "Schematic")
                        # python fstrings are awesome
                        item = f'\t<append xpath="/items">\n\t\t<item name="{k}Schematic">\n\t\t\t<property name="Extends" value="schematicMaster"/>\n\t\t\t<property name="CreativeMode" value="Player"/>\n\t\t\t<property name="CustomIcon" value="{custom_icon}"/>\n\t\t\t<property name="Unlocks" value="{k}"/>\n\t\t\t<effect_group tiered="false">\n\t\t\t\t<triggered_effect trigger="onSelfPrimaryActionEnd" action="ModifyCVar" cvar="{k}" operation="set" value="1"/>\n\t\t\t\t<triggered_effect trigger="onSelfPrimaryActionEnd" action="ModifyCVar" cvar="{k}Schematic" operation="set" value="1"/>\n\t\t\t\t<triggered_effect trigger="onSelfPrimaryActionEnd" action="GiveExp" exp="50"/>\n\t\t\t</effect_group>\n\t\t</item>\n\t</append>'
                        recipe = f'\t\t<recipe name="{k}Schematic" count="1" tags="learnable">\n\t\t\t<ingredient name="resourcePaper" count="3"/>\n\t\t</recipe>'
                        recipes.append(recipe)
                        items.append(item)
                print('\tvalid:         ', valid_tag_schematics)
                print('\tstill invalid: ', still_invalid)

                append_list = ',' + ','.join(valid_tag_schematics)
                prog_mods.append(f'\t<append xpath="progression/perks/perk[@name=\'{name}\']/effect_group/passive_effect[contains(@tags, \'{tags}\')]/@tags">{append_list}</append>')

# schematics_set.remove('medicalBloodDrawKitSchematic')

# create entries for recipes and item appends then add them to the appropriate list
for i in schematics_set:
    recipe = f'\t\t<recipe name="{i}" count="1" tags="learnable">\n\t\t\t<ingredient name="resourcePaper" count="3"/>\n\t\t</recipe>'
    item = f'\t<append xpath="/items/item[@name=\'{i}\']/effect_group">\n\t\t<triggered_effect trigger="onSelfPrimaryActionEnd" action="ModifyCVar" cvar="{i}" operation="set" value="1"/>\n\t</append>'
    recipes.append(recipe)
    items.append(item)

# write files, these ***SHOULD*** be ready to rename and drop into a mod. But ALWAYS double-check
dest_folder = f'Alpha {str(v_num)}/ignore/'
with open(dest_folder + f'A{str(v_num)} copy progression.xml', mode='w') as xml_out:
    xml_out.write('<?xml version="1.0" encoding="UTF-8"?>\n<configs>\n')
    xml_out.write('\n'.join(prog_mods))
    xml_out.write('\n</configs>')

with open(dest_folder + f'A{str(v_num)} copy items.xml', mode='w') as xml_out:
    xml_out.write('<?xml version="1.0" encoding="UTF-8"?>\n<configs>\n\t<append xpath="/items/item[@name=\'schematicMaster\']">\n\t\t<property name="SellableToTrader" value="false"/>\n\t</append>\n')
    xml_out.write('\n'.join(items))
    xml_out.write('\n</configs>')

with open(dest_folder + f'A{str(v_num)} copy recipes.xml', mode='w') as xml_out:
    xml_out.write('<?xml version="1.0" encoding="UTF-8"?>\n<configs>\n\t<append xpath="/recipes">\n')
    xml_out.write('\n'.join(recipes))
    xml_out.write('\n\t</append>\n</configs>')
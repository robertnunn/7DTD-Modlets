import xml.etree.ElementTree as et
import os
import pprint as pp
from PIL import Image, ImageDraw, ImageFont

# takes the POI coords and gets the coords for the label
# this centers the marker (char) on the point specified (x_coord, y_coord)
def marker_coords(char, x_coord, y_coord, font):
    size = font.getsize(char)  # gets a tuple with size of text in pixels (X, Y) (X is horiz, Y is vert)
    x_offset = size[0] // 2  # (integer division)
    y_offset = size[1] // 2  # (integer division)
    coords = (x_coord - x_offset, y_coord - y_offset)  # origin (0,0) is upper left corner
    return coords


# convert between in-game coordinates and pillow coordinates
# in-game coords have their origin at the center, pillow coords have their origin in upper left corner
def convert_coords(map_size, in_game_coords):
    x, y = in_game_coords
    xloc = (map_size//2) + x  # maps are hi-res enough that these rounding errors are negligible
    yloc = (map_size//2) - y
    return (xloc, yloc)


# X is EW, Y is NS
# gets the values from the location string of a POI instance
# returns a tuple
def extract_xy(text):
    xpos = text.find(',')
    ypos = text.rfind(',') + 1
    return (int(text[:xpos]), int(text[ypos:]))


# takes the in-game, internal coordinates (tuple) and formats them to be NS EW coordinates (returns a string)
def pretty_in_game_coords(coord_tuple):
    x, y = coord_tuple
    if x > 0:
        EW = str(x) + "E"  # east is positive
    else:
        EW = str(abs(x)) + "W"  # west is negative
    if y > 0:
        NS = str(y) + "N"  # north is positive
    else:
        NS = str(abs(y)) + "S"  # south is negative
    return NS + " " + EW


path = os.path.dirname(__file__)
print(path)
filename = '/ad2prefabs.xml'
# path = '/ad2prefabs.xml'
os.chdir(path)
path += filename
results = dict()
tree = et.parse(path)
prefabs = tree.findall('./decoration')

for model in prefabs:
    name = model.get('name')
    loc = extract_xy(model.get('position'))
    pretty_loc = pretty_in_game_coords(loc)
    if name in results.keys():
        results[name].append(loc)
    else:
        results[name] = [loc]

output = []
for i in results.keys():
    output.append(str(results[i]) + "," + i)
stuff = '\n'.join(output)

# pp.pprint(results)
with open('Adventure 2 prefab count.txt', mode='w') as out:
    out.write(stuff)

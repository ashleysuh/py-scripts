'''
script for converting gv dot txt file to json 

to run: python parse_dot_to_json.py <filename>

note:
-- 'filename' should be a position text file generated using 'dot' from graphviz
	this dotfile should be generated via a layout algorithm like sfdp, neato, etc.

-- the second half of this script converts the dot file to a json file, with a list
	of nodes and edges that have been parsed from the dot file, with respective
	node coordinate positions

'''

import re
import sys
import os
import json

filename = sys.argv[-1]
nodeCoords = {}
edges = []


with open(filename) as fp:
	line = fp.readline()
	while line:
		if line.find("height") > -1:
			info = line.split()
			node = info[0]

			# get the next line to get position
			line = fp.readline()

			pos = re.findall(r'"(.*?)"', line)
			pos = pos[0]

			coords = pos.split(',')
			x = coords[0]
			y = coords[1]

			nodeCoords[node] = (x,y)			
			line = fp.readline()

		elif line.find("->") > -1:
			info = line.split()
			source = info[0]
			target = info[2]
			edges.append((source,target))
			line = fp.readline()

		else:
			line = fp.readline()


jsonFormat = {}
jsonFormat['nodes'] = []
jsonFormat['links'] = []
jsonFormat['groups'] = []

for node in nodeCoords:
	jsonFormat['nodes'].append({
		'x': nodeCoords[node][0],
		'y': nodeCoords[node][1],
		'id': node,
		'group': 1
		})

for edge in edges:
	jsonFormat['links'].append({
		'source': edge[0],
		'target': edge[1]
		})

outFile = os.path.splitext(filename)[0] + "_sfdp.json"

with open( outFile, 'w') as outfile:
	json.dump(jsonFormat, outfile, indent=4)

##


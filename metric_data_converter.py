'''
converts a regular json file to the file format required by:
https://github.com/VIDILabs/glam
in order to calculate graph aesthetic metrics
'''

import json 
import sys
import os

filename = sys.argv[-1]

nodes = {}
nodeCoords = []
edges = []

n = 1

# need to change the node names to just regular ints
with open(filename) as json_file:
	data = json.load(json_file)
	# creating list of nodes
	for node in data['nodes']:
		# map where nodes[name] = node_index
		id = node['id']
		nodes[id] = n
		n = n+1

		# list where nodes[node_index] = (x, y)
		x = node['x']
		y = node['y']
		nodeCoords.append((x, y))

	# creating list of edges
	for edge in data['links']:
		source = edge['source']
		target = edge['target']
		edges.append((source, target))

#### done with json loading

#### to write to json
metricFormat = {}
metricFormat['nodes'] = []
metricFormat['links'] = []

# this list should be in order
for node in nodeCoords:
	metricFormat['nodes'].append({
		'x': float(node[0]),
		'y': float(node[1])
		})

for edge in edges:
	source = edge[0] # returns a string for node name
	target = edge[1]
	metricFormat['links'].append({
		'source': nodes[source],
		'target': nodes[target]
		})

outFile = os.path.splitext(filename)[0] + "_metricFormat.json"

with open( outFile, 'w') as outfile:
	json.dump(metricFormat, outfile, indent=4)



##


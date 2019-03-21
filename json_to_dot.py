'''
script for converting our data files
to the format required for computing metrics
'''

import json 
import sys
import os

filename = sys.argv[-1]

nodes = {}
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

	# creating list of edges
	for edge in data['links']:
		source = edge['source']
		target = edge['target']
		edges.append((source, target))

#### done with json loading


outFile = os.path.splitext(filename)[0] + "_gv.txt"

file = open(outFile, "w")

file.write("digraph G {\n")

for edge in edges:
	source = edge[0] # returns a string for node name
	target = edge[1]
	if source != target:
		file.write("   " + str(nodes[source]) + " -> " + str(nodes[target]) + ";\n") 		

file.write("}") 

file.close() 




##


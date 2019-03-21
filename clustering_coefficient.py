'''
script to compute the average clustering coefficient
first need to convert json-formatted graphs to a networkx graph

to run:

python clustering_coefficient.py <filename.json>
'''
import networkx as nx
import json 
import sys
import os


nodes = {}
edges = []

n = 1

filename = sys.argv[-1]

# need to change the node names to just regular ints
with open(filename) as json_file:
	data = json.load(json_file)
	# creating list of nodes
	for node in data['nodes']:
		# map where nodes[name] = node_index
		id = node['id']
		nodes[id] = n
		n = n+1

	# creating list of edges where source,target are the node indices
	for edge in data['links']:
		source = edge['source']
		target = edge['target']
		edges.append((nodes[source], nodes[target]))

# create graph in networkX
G = nx.Graph()

for node in nodes:
	G.add_node(nodes[node])

for edge in edges:
	G.add_edge(edge[0], edge[1])

avg_clustering_coeff = nx.average_clustering(G)

print(avg_clustering_coeff)
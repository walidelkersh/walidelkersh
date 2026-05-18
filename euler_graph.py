import networkx as nx
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay
import numpy as np
import random

# 1. Generate guaranteed planar graph using Delaunay Triangulation
points = np.random.rand(12, 2) # 12 random vertices
tri = Delaunay(points)

G = nx.Graph()
for path in tri.simplices:
    G.add_edge(path[0], path[1])
    G.add_edge(path[1], path[2])
    G.add_edge(path[2], path[0])

# Randomly thin out edges but keep it connected to vary the shape
spanning_tree = nx.minimum_spanning_tree(G)
final_graph = nx.Graph(spanning_tree)
remaining_edges = [e for e in G.edges() if not final_graph.has_edge(*e)]
k_extra = random.randint(2, len(remaining_edges))
final_graph.add_edges_from(random.sample(remaining_edges, k=k_extra))

V = final_graph.number_of_nodes()
E = final_graph.number_of_edges()
F = 2 - V + E  # Euler's formula for connected planar graph

# 2. Plotting the Graph (Beautiful dark mode styling with extra bottom padding)
fig = plt.figure(figsize=(6, 5), facecolor='none')
ax = fig.add_axes([0, 0.2, 1, 0.8])
ax.axis('off')

pos = {i: points[i] for i in range(len(points))}
nx.draw_networkx_nodes(final_graph, pos, node_color='#36BCF7', node_size=300, edgecolors='white', linewidths=1.5)
nx.draw_networkx_edges(final_graph, pos, edge_color='#A0ABC0', width=2)

# Render Euler math formulas directly inside the transparent PNG image
fig.text(0.5, 0.12, "V - E + F = 2", color='#9745f5', fontsize=18, fontweight='bold', ha='center', fontfamily='sans-serif')
fig.text(0.5, 0.04, f"For the graph above: {V} - {E} + {F} = 2", color='#A0ABC0', fontsize=12, ha='center', fontfamily='sans-serif')

plt.savefig('euler_graph.png', transparent=True, format='png', dpi=150)
plt.close()

import networkx as nx
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay
import numpy as np
import random
import re

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

# 2. Plotting the Graph (Beautiful dark mode styling)
fig = plt.figure(figsize=(6, 4), facecolor='none')
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('off')

pos = {i: points[i] for i in range(len(points))}
nx.draw_networkx_nodes(final_graph, pos, node_color='#36BCF7', node_size=300, edgecolors='white', linewidths=1.5)
nx.draw_networkx_edges(final_graph, pos, edge_color='#A0ABC0', width=2)

plt.savefig('euler_graph.png', transparent=True, format='png', dpi=150)
plt.close()

# 3. Update the README.md dynamically
with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

# Replace the math equation using regex between HTML comments
pattern = r"<!-- MATH_START -->.*?<!-- MATH_END -->"
new_math = f"<!-- MATH_START -->\n  <h2 align=\"center\"> $$V - E + F = 2$$ </h2>\n  <h4 align=\"center\"> For the graph below: $${V} - {E} + {F} = 2$$ </h4>\n  <!-- MATH_END -->"

updated_readme = re.sub(pattern, new_math, readme, flags=re.DOTALL)

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(updated_readme)

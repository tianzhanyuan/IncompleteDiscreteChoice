import networkx as nx
import idclib as idc

# Define the Y-nodes and U-nodes
Y_nodes = [(0,0),(0,1),(1,0),(1,1)]
U_nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g']  # <-- include 'g' to match edges

# Add edges between nodes
edges = [
    ('a', (0,0)),
    ('b', (0,1)),
    ('c', (0,0)),
    ('c', (1,0)),
    ('d', (0,0)),
    ('d', (1,1)),
    ('e', (0,1)),
    ('e', (1,1)),
    ('f', (1,0)),
    ('g', (1,1)),
]

# idc library has a class BipartiteGraph to store your model
gmodel = idc.BipartiteGraph(Y_nodes, U_nodes, edges)

# Plot the graph using the new method
gmodel.plot_graph(title='Panel DC Example')



# Build the bipartite graph with required node attribute 'type'
B = nx.Graph()
B.add_nodes_from(Y_nodes, type=0)   # Y side
B.add_nodes_from(U_nodes, type=1)   # U side
B.add_edges_from(edges)

# Sanity checks for compatibility
missing_type = [n for n in B.nodes if 'type' not in B.nodes[n]]
if missing_type:
    raise ValueError(f"These nodes are missing the required 'type' attribute: {missing_type}")

bad_edges = [(u,v) for (u,v) in B.edges if B.nodes[u]['type'] == B.nodes[v]['type']]
if bad_edges:
    raise ValueError(f"These edges are not bipartite (connect same type): {bad_edges}")

# Compute smallest core-determining class
cdc = gmodel.smallest_CDC()

# Print nicely (sorted by size then lexicographically)
cdc_sorted = sorted(cdc, key=lambda s: (len(s), s))
print("Smallest CDC (as subsets of Y):")
for s in cdc_sorted:
    print(s)
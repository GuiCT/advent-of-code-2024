import networkx

with open("23/input.txt", "r") as f:
    lines = f.read().splitlines()

# NetworkX, cause i'm lazy. Sorry
connections_graph = networkx.graph.Graph()
for l in lines:
    u, v = l.split('-')
    connections_graph.add_edge(u, v)

# I just learned something today.
# How I never heard about "Cliques", well...
# I don't know
all_cliques = list(networkx.enumerate_all_cliques(connections_graph))
nodes_with_t = set([n for n in connections_graph.nodes if n.startswith('t')])
amount_cliques = 0
for clique3 in filter(lambda c: len(c) == 3, all_cliques):
    nodes = set(clique3)
    has_node_with_t = len(nodes.intersection(nodes_with_t)) > 0
    if has_node_with_t:
        amount_cliques += 1

print("Part 1 result", amount_cliques)

# Part 2
# NetworkX MVP
max_clique = max(all_cliques, key=lambda c: len(c))
ordered_max_clique = sorted(max_clique)
print("Part 2 result", ",".join(ordered_max_clique))

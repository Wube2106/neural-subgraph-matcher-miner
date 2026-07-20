import networkx as nx
import pickle
import gzip

G = nx.Graph()
with gzip.open("ca-HepTh.txt.gz", "rt") as f:
    for line in f:
        if line.startswith("#"):
            continue
        a, b = line.strip().split("\t")
        G.add_edge(int(a), int(b))

print(f"Loaded {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")
with open("ca_hepth.pkl", "wb") as f:
    pickle.dump(G, f)

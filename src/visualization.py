import matplotlib.pyplot as plt
import networkx as nx


def plot_coupling_map(proc, out_path):
    g = nx.Graph()
    g.add_nodes_from(range(proc["num_qubits"]))
    g.add_edges_from(tuple(e) for e in proc["coupling_map"])
    plt.figure(figsize=(5, 4))
    nx.draw(g, with_labels=True, node_size=900, node_color="#cfe3ff")
    plt.title(f'{proc["name"]} ({proc["num_qubits"]} qubits)')
    plt.savefig(out_path, dpi=200, bbox_inches="tight")
    plt.close()

import matplotlib.pyplot as plt
import networkx as nx

def plot_graph(graph):
    # Create a directed graph (DiGraph) since our original implementation was directed
    G = nx.DiGraph()

    # Add edges to the networkx graph
    for vertex in graph:
        for neighbor in graph[vertex]:
            G.add_edge(vertex, neighbor)

    # Draw the graph
    pos = nx.spring_layout(G, seed=29)  # Consistent layout
    nx.draw(G, pos, with_labels=True, node_size=1500, node_color='lightblue',
            font_size=12, font_weight='bold', arrowsize=20)

    plt.title("Graph Visualization")
    plt.show()

def plot_runtimes(array_sizes, runtimes):
    plt.figure(figsize=(10, 6))
    for algorithm, time in runtimes.items():
        # Pair upsizes and times, skip None entries
        paired = [(s, t) for s, t in zip(array_sizes, time) if t is not None]
        if not paired:
            continue
        xs, ys = zip(*paired)
        plt.plot(xs, ys, marker='o', label=algorithm, linewidth=2)
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Input Size (n)', fontsize=12)
    plt.ylabel('Average Time (s)', fontsize=12)
    plt.title('Sorting Algorithm Runtimes (Log-Log Scale)', fontsize=14)
    plt.legend(fontsize=10)
    plt.grid(True, which='both', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

def plot_tree(tree):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')

    def do_plot(node, x, y, dx, level):
        if node is None:
            return
        ax.text(x, y, str(node.value), ha='center', va='center',
                bbox=dict(facecolor='skyblue', boxstyle='circle'))

        if node.left:
            child_x = x - dx
            child_y = y - 1
            ax.plot([x, child_x], [y, child_y], 'k-')
            do_plot(node.left, child_x, child_y, dx / 2, level + 1)
        if node.right:
            child_x = x + dx
            child_y = y - 1
            ax.plot([x, child_x], [y, child_y], 'k-')
            do_plot(node.right, child_x, child_y, dx / 2, level + 1)

    do_plot(tree.root, x=0, y=0, dx=4, level=0)
    plt.show()
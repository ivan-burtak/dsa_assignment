from algorithms import quick_sort, BinarySearchTree, heap_sort, Graph, bfs
from plots import plot_tree, plot_graph

# 1. Quick Sort
arr = [5, 3, 8, 4, 2]
quick_sort(arr)
print("Sorted:", arr)

# 2. Binary Search Tree
bst = BinarySearchTree()
for val in [7, 3, 9, 9, 10, 1, 5]:
    bst.insert(val)

plot_tree(bst)
print("Inorder traversal:", bst.inorder())

# Search for a value
key = 5
found = bst.search(key)
print(f"Search {key}: {'Found' if found else 'Not found'}")

# 3. Heap Sort
arr = [4, 10, 3, 5, 1]
heap_sort(arr)
print("Sorted:", arr)

# 4. Breadth-First Search
graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)
plot_graph(graph)

print("BFS path:", bfs(graph, 1))
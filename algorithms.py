from collections import deque

# --------------------------------
# Quick Sort
# --------------------------------

# in place
def quick_sort(arr, low=0, high=None): # Time: O(n*log(n)), Space: O(n)
    if high is None:  # high should be none on the first call of the function so that it gets initialized with the length of the unsorted array
        high = len(arr) - 1

    if low < high:  # only run if the array has more than 1 element
        pivot_i = partition(arr, low, high)  # place the pivot (last element) in its final sorted position
        quick_sort(arr, low, pivot_i - 1)  # recursively sort the left and right of the pivot
        quick_sort(arr, pivot_i + 1, high)


# in place quicksort is used because its faster and takes less memory
def partition(arr, low, high):
    pivot = arr[high]  # choosing the last element as the pivot
    i = low - 1  # i is the -1st index
    for j in range(low, high):  # going through each element and if arr[j] is smaller than the pivot, i += 1 and switch i and j
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # switch the pivot to its sorted position in the array
    return i + 1

# --------------------------------
# Binary Search Tree
# --------------------------------

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._do_insert(self.root, key)

    def _do_insert(self, node, key):
        if node is None:
            return TreeNode(key)
        if key < node.value:
            node.left = self._do_insert(node.left, key)
        else:
            node.right = self._do_insert(node.right, key)
        return node

    def inorder(self):
        return self._do_inorder(self.root)

    def _do_inorder(self, node):
        if node is None:
            return []
        return self._do_inorder(node.left) + [node.value] + self._do_inorder(node.right)

    def search(self, key):
        return self._do_search(self.root, key)

    def _do_search(self, node, key):
        if node is None or node.value == key:
            return node
        if key < node.value:
            return self._do_search(node.left, key)
        else:
            return self._do_search(node.right, key)

# --------------------------------
# Heap Sort
# --------------------------------

def left_child(i):
    return 2 * i + 1

def right_child(i):
    return 2 * i + 2

def parent(i):
    return 0 if i == 0 else (i - 1) // 2

def heapify(arr, size, node):
    max_i = node
    left_i = left_child(node)
    right_i = right_child(node)

    if left_i < size and arr[left_i] > arr[max_i]:  # compare index and value with children and assign index to largest
        max_i = left_i

    if right_i < size and arr[right_i] > arr[max_i]:
        max_i = right_i

    if max_i != node:
        arr[node], arr[max_i] = arr[max_i], arr[node]  # swap
        heapify(arr, size, max_i)


def build_heap(arr):
    size = len(arr)  # defined here so that it does not need to be calculated every time in the loop (saves time)
    last_non_leaf = parent(size - 1)
    for node in range(last_non_leaf, -1, -1):  # starting from the last non leaf node (till -1 because range is not inclusive)
        heapify(arr, size, node)

def heap_sort(arr): # Time: O(n*log(n)), Space: O(1)
    build_heap(arr)
    for end_i in range(len(arr) - 1, 0, -1):
        arr[0], arr[end_i] = arr[end_i], arr[0]
        heapify(arr, end_i, 0)


# --------------------------------
# Graph
# --------------------------------

class Graph:
    def __init__(self, adjacency = None):
        self.adjacency = adjacency or {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency:
            self.adjacency[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.adjacency:
            self.add_vertex(vertex1)
        if vertex2 not in self.adjacency:
            self.add_vertex(vertex2)
        self.adjacency[vertex1].append(vertex2)

    def __iter__(self):
        return iter(self.adjacency)

    def __getitem__(self, vertex):
        return self.adjacency[vertex]

# --------------------------------
# Breadth-First Search
# --------------------------------

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    path = []

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            path.append(vertex)

            neighbors = sorted(graph[vertex])
            for neighbor in neighbors:
                if neighbor in visited:
                    continue
                queue.append(neighbor)

    return path


# --------------------------------
# Merge Sort
# --------------------------------

# note: returns the sorted array instead of just editing the one that's passed into it
def merge_sort(arr):  # Time: O(n*log(n)), Space: O(n)
    if len(arr) <= 1:  # base case
        return arr

    mid = len(arr) // 2  # divide the array in half
    left_half = arr[:mid]
    right_half = arr[mid:]

    sorted_left = merge_sort(left_half)  # recursion
    sorted_right = merge_sort(right_half)

    return merge(sorted_left, sorted_right)  # merge each pair of arrays

def merge(arr1, arr2):
    result = []  # empty array
    i = j = 0
    while i < len(arr1) and j < len(arr2):  # iterating through each array to compare the values
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
            continue
        if arr1[i] > arr2[j]:
            result.append(arr2[j])
            j += 1
            continue
        # if they have the same value
        result.append(arr1[i])
        result.append(arr2[j])
        i += 1
        j += 1

    while i < len(arr1):  # dealing with leftover values if one list is longer than the other
        result.append(arr1[i])
        i += 1

    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result

# --------------------------------
# Insertion Sort
# --------------------------------
def insertion_sort(arr):  # Time: O(n**2), Size: O(1)
    for i in range(1, len(arr)):
        val = arr[i]  # store the key in a variable
        j = i - 1
        while j >= 0 and arr[j] > val:  # loop backwards through the sorted version, shifting the elements right
            arr[j + 1] = arr[j]  # shift elements right by copying the value of j to j + 1
            j -= 1  # reduce j by 1
        arr[j + 1] = val  # because of the previous steps j + 2 = j + 1, so j + 1 should be the key value
        '''
        [j, i, ...]
        [3, 2, 1]
        key = 2, j = 0
        [3, 3, 1] key = 2 j = -1 (because j = -1 we exit the loop)
        j + 1 = 0, so arr[0] = key
        [2, 3, 1]
        '''
    return arr
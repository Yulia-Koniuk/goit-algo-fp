import uuid
import networkx as nx
import matplotlib.pyplot as plt

class MaxHeapNode:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_max_heap_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_max_heap_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_max_heap_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def build_max_heap(array):
    heap_root = None
    for item in array:
        heap_root = max_heap_insert(heap_root, item)
    return heap_root

def max_heap_insert(root, key):
    new_node = MaxHeapNode(key)
    if root is None:
        return new_node
    
    # Додаємо новий вузол в кінець купи
    q = [root]
    while len(q) > 0:
        temp = q.pop(0)
        if temp.left is None:
            temp.left = new_node
            break
        else:
            q.append(temp.left)
        if temp.right is None:
            temp.right = new_node
            break
        else:
            q.append(temp.right)

    # Піднімаємо вузол вгору, доки він не досягне свого правильного місця
    current = new_node
    while current != root:
        parent = find_parent(root, current)
        if parent.val < current.val:
            current.val, parent.val = parent.val, current.val
            current = parent
        else:
            break
    return root

def find_parent(root, node):
    # Знаходимо батьківський вузол для даного вузла
    if root is None or root == node:
        return None
    if root.left == node or root.right == node:
        return root
    left_parent = find_parent(root.left, node)
    if left_parent is not None:
        return left_parent
    return find_parent(root.right, node)

def draw_max_heap(heap_root):
    heap_tree = nx.DiGraph()
    pos = {heap_root.id: (0, 0)}
    heap_tree = add_max_heap_edges(heap_tree, heap_root, pos)

    colors = [node[1]['color'] for node in heap_tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in heap_tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(heap_tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


# Створення максимальної купи з заданих елементів
heap_array = [30, 20, 25, 10, 5, 15, 7, 17, 2, 33, 18, 18, 1, 29, 15]
heap_root = build_max_heap(heap_array)
draw_max_heap(heap_root)




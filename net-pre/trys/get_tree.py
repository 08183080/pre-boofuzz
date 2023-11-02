import networkx as nx
import matplotlib.pyplot as plt

"""
成功实现多序列合并实现序列树
"""

class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.children = []

def add(self, l: list):
    n = len(l)
    current_node = self

    for i in range(1, n):
        found = False
        for child in current_node.children:
            if child.value == l[i]:
                current_node = child
                found = True
                break

        if not found:
            new_node = TreeNode(l[i])
            current_node.children.append(new_node)
            current_node = new_node

    return self

def visualize_protocol_tree(root):
    G = nx.Graph()

    def traverse(node, parent=None):
        G.add_node(node.value)

        if parent:
            G.add_edge(parent.value, node.value)

        for child in node.children:
            traverse(child, node)

    traverse(root)
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500, font_size=10, font_weight='bold', edge_color='gray', width=1.5)
    plt.show()

if __name__ == "__main__":
    t = TreeNode(1)
    s1 = [1, 0, 2]
    s2 = [1, 0, 3]
    s3 = [1, 0, 4, 5]
    s4 = [1, 6]
    # s5 = [1, 7, 9, 2]
    t = add(t, s1)
    t = add(t, s2)
    t = add(t, s3)
    t = add(t, s4)
    # t = add(t, s5)

    visualize_protocol_tree(t)
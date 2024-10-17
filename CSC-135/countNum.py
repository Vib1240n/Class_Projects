class node:
    def __init__(self, data):
        self.data = data
        self.children = None
    
    def add_child(self, child):
        if self.children == None:
            self.children = []
        self.children.append(child)
        
    def __str__(self) -> str:
    # The tail end of the list
        current = self.children
        in_list = "(" + str(self.data)
        while current is not None:
            in_list += ', ' + str(current.data)
        return in_list + ")"

    def is_leaf(self):
        return self.children == None
    
    
def num_leaves(tree_node):
    i = 0
    if not tree_node.is_leaf():
        for j in tree_node.children:
            i = i + 1
            num_leaves(j)
    return i


leaf = node(1)
leaf.add_child(2)
leaf.add_child(4)
leaf.add_child(5)
leaf.add_child(6)
leaf.add_child(7)
leaf.add_child(8)

print(leaf)

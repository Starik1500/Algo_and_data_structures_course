class BinaryTree:
    def __init__(self, value: int):
        self.value = value
        self.right = None
        self.left = None


def invert_binary_tree(node):
    if node is None:
        return None
    else:
        node.left, node.right = node.right, node.left
        invert_binary_tree(node.right)
        invert_binary_tree(node.left)
    return node


def printing_result(node):
    if node is not None:
        print(node.value, end=" ")
        printing_result(node.left)
        printing_result(node.right)


root = BinaryTree(9)
root.left = BinaryTree(6)
root.right = BinaryTree(3)

invert_binary_tree(root)
printing_result(root)

class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None


class PriorityQueue:
    def __init__(self):
        self.root = None

    def insert(self, value, priority):
        if not self.root:
            self.root = Node(value, priority)
            return
        self._insert_recursive(self.root, value, priority)

    def _insert_recursive(self, node, value, priority):
        if priority <= node.priority:
            if node.left is None:
                node.left = Node(value, priority)
            else:
                self._insert_recursive(node.left, value, priority)
        else:
            if node.right is None:
                node.right = Node(value, priority)
            else:
                self._insert_recursive(node.right, value, priority)

    def pop(self):
        if not self.root:
            return None
        max_node = self._find_max(self.root)
        self._remove_max(self.root, max_node)
        return max_node.value

    def _find_max(self, node):
        if node.right is None:
            return node
        return self._find_max(node.right)

    def _remove_max(self, node, max_node):
        if node.right is max_node:
            node.right = max_node.left
        elif node.left is max_node:
            node.left = max_node.left
        else:
            self._remove_max(node.right, max_node)

    def peek(self):
        if not self.root:
            return None
        return self._find_max(self.root).value

    def inorder_traversal(self):
        values = []
        self._inorder_traversal_recursive(self.root, values)
        return values

    def _inorder_traversal_recursive(self, node, values):
        if node:
            self._inorder_traversal_recursive(node.left, values)
            values.append((node.value, node.priority))
            self._inorder_traversal_recursive(node.right, values)


if __name__ == "__main__":
    pq = PriorityQueue()
    pq.insert(5, 3)
    pq.insert(2, 1)
    pq.insert(3, 2)
    pq.insert(4, 5)
    pq.insert(5, 4)

    print("До видалення:")
    print(pq.inorder_traversal())

    print("Останній пріорітет:", pq.peek())

    print("Видаляє:", pq.pop())
    print("Після видалення:")
    print(pq.inorder_traversal())

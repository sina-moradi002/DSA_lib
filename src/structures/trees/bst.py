from src.structures.trees.tree_node import TreeNode
from src.structures.trees.binary_tree import BinaryTree


class BinarySearchTree(BinaryTree):

    def __init__(self):
        super().__init__()
        self.min = None
        self.max = None

    # Private Methods
    def _update_max_min(self):
        """Update maximum and minimum nodes after deletion"""
        self.min = self.find_min()
        self.max = self.find_max()

    def _get_height(self, node):
        """Calculate the height of tree recursively"""
        if node is None:
            return -1
        return 1 + max(self._get_height(node.left), self._get_height(node.right))

    def _preorder(self, node, result):
        """Preorder Traversal"""
        if node:
            result.append(node.data)
            self._preorder(node.left, result)
            self._preorder(node.right, result)

    def _inorder(self, node, result):
        """Inorder Traversal"""
        if node:
            self._inorder(node.left, result)
            result.append(node.data)
            self._inorder(node.right, result)

    def _postorder(self, node, result):
        """Postorder Traversal"""
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.data)

    def _find_min_node(self, node):
        """Minimum Node in given subtree"""
        curr = node
        while curr and curr.left:
            curr = curr.left
        return curr

    def _delete(self, node, key):
        """Delete a key recursively and return the new node"""
        if node is None:
            return None

        if key < node.data:
            node.left = self._delete(node.left, key)
            if node.left:
                node.left.parent = node
        elif key > node.data:
            node.right = self._delete(node.right, key)
            if node.right:
                node.right.parent = node
        else:
            self.size -= 1
            if node.left is None:
                right_child = node.right
                if right_child:
                    right_child.parent = node.parent
                return right_child
            elif node.right is None:
                left_child = node.left
                if left_child:
                    left_child.parent = node.parent
                return left_child
            else:
                succ = self._find_min_node(node.right)
                node.data = succ.data
                node.right = self._delete(node.right, succ.data)
                if node.right:
                    node.right.parent = node
                self.size += 1
        return node

    # Public Methods
    def is_empty(self):
        return self.root is None

    def get_size(self):
        return self.size

    def get_hight(self):
        return self._get_height(self.root)

    def preorder(self):
        lst = []
        self._preorder(self.root, lst)
        return lst

    def inorder(self):
        lst = []
        self._inorder(self.root, lst)
        return lst

    def postorder(self):
        lst = []
        self._postorder(self.root, lst)
        return lst

    def insert(self, value):
        new_node = TreeNode(value)

        if self.root is None:
            self.root = new_node
            self.size = 1
            self.min = value
            self.max = value
            return

        curr = self.root
        parent = None
        while curr:
            parent = curr
            if value < curr.data:
                curr = curr.left
            elif value > curr.data:
                curr = curr.right
            else:
                return

        if value < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node
        new_node.parent = parent

        self.size += 1

        if value > self.max:
            self.max = value
        if value < self.min:
            self.min = value

    def delete(self, value):
        if self.root is None:
            return
        self.root = self._delete(self.root, value)
        if self.root is None:
            self.min = None
            self.max = None
        else:
            self._update_max_min()

    def search(self, value):
        curr = self.root
        while curr:
            if value == curr.data:
                return True
            elif value < curr.data:
                curr = curr.left
            else:
                curr = curr.right
        return False

    def find_max(self):
        if self.root is None:
            return None
        curr = self.root
        while curr.right:
            curr = curr.right
        return curr.data

    def find_min(self):
        if self.root is None:
            return None
        curr = self.root
        while curr.left:
            curr = curr.left
        return curr.data

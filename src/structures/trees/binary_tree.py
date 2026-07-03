from src.structures.trees.tree_node import TreeNode
from src.structures.queue import queue

class BinaryTree:
    # EXP:   root
    #         5
    #        / \
    #       6   2
    #      / \
    #     7   9
    # size = 5 , height = 3 , min = 2 , max = 9
    # NOTE: This data structure is not too efficient and useful, but we develop it
    # for educational purposes and for BST Inheritance

    # Attribute of a list
    def __init__(self):
        self.root = None
        self.size = 0
        self.max = 0
        self.min = 0

    # Private function
    # Update min and max after deletion
    def _update_min_max(self):
        if self.root is None:
            self.min = 0
            self.max = 0
            return

        q = queue()
        q.enqueue(self.root)

        self.min = self.root.data
        self.max = self.root.data

        while not q.is_empty():
            curr = q.dequeue()

            if curr.data < self.min:
                self.min = curr.data

            if curr.data > self.max:
                self.max = curr.data

            if curr.left is not None:
                q.enqueue(curr.left)

            if curr.right is not None:
                q.enqueue(curr.right)

    # True if size is empty / False otherwise
    def is_empty(self):
        return self.size == 0

    # Return the size of tree
    def get_size(self):
        return self.size

    # Find tree height by recursion method
    def get_height(self, root):
        if self.root is None:
            return -1

        # compute the height of left and right subtrees
        if root.left is not None:
            lHeight = self.get_height(root.left)
        else:
            lHeight = 0

        if root.right is not None:
            rHeight = self.get_height(root.right)
        else:
            rHeight = 0

        return max(lHeight, rHeight) + 1

    def preorder(self, root):
        if root is None:
            return []

        ls = [root.data]
        ls += self.preorder(root.left)
        ls += self.preorder(root.right)
        return ls

    def inorder(self, root):
        if root is None:
            return []

        ls = []
        ls += self.inorder(root.left)
        ls.append(root.data)
        ls += self.inorder(root.right)
        return ls

    def postorder(self, root):
        if root is None:
            return []

        ls = []
        ls += self.postorder(root.left)
        ls += self.postorder(root.right)
        ls.append(root.data)
        return ls

    def insert(self, value):
        new_node = TreeNode(value)
        if self.root is None:
            self.root = new_node
            self.size = 1
            self.max = value
            self.min = value
            return

        q = queue()
        q.enqueue(self.root)

        while not q.is_empty():
            curr = q.dequeue()
            if curr.left is not None:
                q.enqueue(curr.left)
            else:
                curr.left = new_node
                self.size += 1
                if new_node.data < self.min:
                    self.min = new_node.data
                elif new_node.data > self.max:
                    self.max = new_node.data
                return

            if curr.right is not None:
                q.enqueue(curr.right)
            else:
                curr.right = new_node
                self.size += 1
                if new_node.data < self.min:
                    self.min = new_node.data
                elif new_node.data > self.max:
                    self.max = new_node.data
                return

   #TODO: add deletion function

    def search(self, value):
        # Return False if the tree is empty
        if self.root is None:
            return False

        # creating a queue
        q = queue()
        # enqueue the root
        q.enqueue(self.root)

        # Search every node with a level‑order traversal to find out if 'value' is tree or not
        while not q.is_empty():
            curr = q.dequeue()
            # return if current node is the target. Value Found!
            if curr.data == value:
                return True

            # enqueue children
            if curr.left is not None:
                q.enqueue(curr.left)
            if curr.right is not None:
                q.enqueue(curr.right)

        # Value Not Found!
        return False


    def find_max (self):
        return self.max

    def find_min (self):
        return self.min

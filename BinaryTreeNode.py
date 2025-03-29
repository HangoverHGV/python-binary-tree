class BinaryTreeNode:
    def __init__(self, value, level=0):
        self.value = value
        self.left = None
        self.right = None
        self.sibling = None
        self.level = level
        self.parent = None
        self.children = []

    def add_left(self, node, force=False):
        if node == self:
            node = BinaryTreeNode(self.value)
        if not force:
            if self.left is not None:
                raise ValueError("Left child already exists")
        self.left = node
        node.level = self.level + 1
        node.parent = self
        if node not in self.children:
            self.children.append(node)

    def add_right(self, node, force=False):
        if node == self:
            node = BinaryTreeNode(self.value)
        if not force:
            if self.right is not None:
                raise ValueError("Right child already exists")
        self.right = node
        node.level = self.level + 1
        node.parent = self
        if node not in self.children:
            self.children.append(node)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

    def __eq__(self, other):
        if isinstance(other, BinaryTreeNode):
            return self.value == other.value
        return False

    def __ne__(self, other):
        if isinstance(other, BinaryTreeNode):
            return self.value != other.value
        return True

    def __lt__(self, other):
        if isinstance(other, BinaryTreeNode):
            return self.value < other.value
        return False

from BinaryTreeNode import BinaryTreeNode
from BinaryTree import BinaryTree



if __name__ == '__main__':
    bt = BinaryTree()
    root = BinaryTreeNode(0)
    node1 = BinaryTreeNode(1)
    node2 = BinaryTreeNode(2)
    node3 = BinaryTreeNode(3)
    node4 = BinaryTreeNode(4)

    root.add_left(node1)
    root.add_right(node2)

    node1.add_right(node3)
    node2.add_right(node4)

    bt.insert(root)
    bt.insert(node1)
    bt.insert(node2)

    print(bt)
    bt.draw()





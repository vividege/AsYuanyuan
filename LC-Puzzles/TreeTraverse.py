from queue import Queue


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


####前序遍历-递归算法
def preOrder(node: TreeNode):
    if node == None:
        return

    print(node.val)

    preOrder(node.left)
    preOrder(node.right)


####中序遍历-递归算法
def inOrder(node: TreeNode):
    if node == None:
        return

    inOrder(node.left)
    print(node.val)
    inOrder(node.right)


####后续遍历-递归算法
def postOrder(node: TreeNode):
    if node == None:
        return

    postOrder(node.left)
    postOrder(node.right)
    print(node.val)


####层序遍历
def layerOrder(node: TreeNode):
    q = list(node)
    while 0 < len(q):
        n = q.pop(0)
        print(n.val)
        if not n.left:
            q.append(n.left)
        if not n.right:
            q.append(n.right)

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        def _insert(node, val):
            if not node:
                return TreeNode(val)
            if val <= node.val:
                node.left = _insert(node.left, val)
            elif val > node.val:
                node.right = _insert(node.right, val)
            return node

        self.root = _insert(self.root, val)

    def inorder(self):
        res = []

        def _inorder(node):
            if node:
                _inorder(node.left)
                res.append(node.val)
                _inorder(node.right)

        _inorder(self.root)
        return res

    def preorder(self):
        res = []

        def _preorder(node):
            if not node:
                return
            res.append(node.val)
            _preorder(node.left)
            _preorder(node.right)

        _preorder(self.root)
        return res

    def postorder(self):
        res = []

        def _postorder(node):
            if not node:
                return
            _postorder(node.left)
            _postorder(node.right)
            res.append(node.val)

        _postorder(self.root)
        return res


if __name__ == '__main__':
    bst = BST()
    bst.insert(1)
    bst.insert(3)
    bst.insert(2)
    bst.insert(4)

    path = bst.inorder()
    print(path)

    path = bst.preorder()
    print(path)

    path = bst.postorder()
    print(path)

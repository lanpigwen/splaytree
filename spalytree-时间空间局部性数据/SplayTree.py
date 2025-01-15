class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class SplayTree(object):
    def __init__(self):
        self.root = None
        self.size = 0


    def RightRotate(self, x):
        if x is None or x.left is None:
            return x
        y = x.left
        x.left = y.right
        y.right = x

        return y

    def LeftRotate(self, x):
        if x is None or x.right is None:
            return x
        y = x.right
        x.right = y.left
        y.left = x

        return y

    def splay(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            if root.left is None:
                return root
            if key < root.left.key:
                root.left.left = self.splay(root.left.left, key)
                root = self.RightRotate(root)
            elif key > root.left.key:
                root.left.right = self.splay(root.left.right, key)
                root.left = self.LeftRotate(root.left)
            return root if root.left is None else self.RightRotate(root)
        else:
            if root.right is None:
                return root
            if key < root.right.key:
                root.right.left = self.splay(root.right.left, key)
                if root.right.left:
                    root.right = self.RightRotate(root.right)
            elif key > root.right.key:
                root.right.right = self.splay(root.right.right, key)
                root = self.LeftRotate(root)
            return root if root.right is None else self.LeftRotate(root)

    def search(self, key):
        self.root = self.splay(self.root, key)

    def insert(self, key):
        self.size += 1
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return Node(key)
        root = self.splay(root, key)
        if root.key == key:
            return root
        new = Node(key)
        if root.key > key:
            new.right = root
            new.left = root.left
            root.left = None
        else:
            new.left = root
            new.right = root.right
            root.right = None

        return new

    def delete(self, key):
        self.root = self.splay(self.root, key)
        if self.root is None or self.root.key != key:
            return
        if self.root.left is None:
            self.root = self.root.right
        else:
            x = self.root.right
            self.root = self.root.left
            self.root = self.splay(self.root, key)


    def split(self, key):
        self.root = self.splay(self.root, key)
        if key != self.root.key:
            return None, None
        left, right = self.root.left, self.root.right
        return left, right

    def join(self, left, right):
        if left is None or right is None:
            return left if left else right
        maxElem = left.findMax()
        minElem = right.findMin()
        assert maxElem < minElem
        right.left = left
        return right

    def findMin(self):
        if self.root is None:
            return None
        x = self.root
        while x.left:
            x = x.left

        self.root = self.splay(self.root, x.key)
        return x.key

    def findMax(self):
        if self.root is None:
            return None
        x = self.root
        while x.right:
            x = x.right

        self.root = self.splay(self.root, x.key)
        return x.key

    def seq_op(self, seqs, ops):
        opt = ['search', 'insert', 'delete']
        for i in range(len(ops)):
            op = ops[i]
            seq = seqs[i]
            if op == 0:
                self.search(seq)
            elif op == 1:
                self.insert(seq)
            elif op == 2:
                self.delete(seq)

    def preorder(self, subtree):
        if subtree:
            print(subtree.key, end=' ')
            self.preorder(subtree.left)
            self.preorder(subtree.right)
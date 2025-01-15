import copy
# from view import draw
from genTask import getTaskSeq

class TreeNode():
    def __init__(self, x=None):
        self.key = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.key)


class BST():
    def __init__(self, node=None):
        # node = TreeNode(node)
        self.root = None
        self.size = 0

    def is_leaf(self,node):

        return node is not None and node.left is None and node.right is None

    def insert(self, x):
        self.size += 1
        self.root = self._insert(self.root, x)

    def _insert(self, root, x):
        global opStep
        p = TreeNode(x)
        if root == None:
            root = p
        elif x < root.key:
            root.left = self._insert(root.left, x)
        elif x > root.key:
            root.right = self._insert(root.right, x)
        else:
            self.size-=1
        return root


    def search(self,x):
        return self._search(self.root,x)

    def _search(self,root, x):
        if root is None:
            return None
        if root.key==x:
            return root
        elif x<root.key:
            return self._search(root.left,x)
        else:
            return self._search(root.right, x)

    def findMax(self,node):
        if node == None:
            return None
        while node.right != None:
            node = node.right
        return node

    def findMin(self,node):
        if node == None:
            return None
        while node.left != None:
            node = node.left
        return node

    def delete(self, x):
        self.root = self._delete(self.root, x)

    def _delete(self, node, x):
        if node is None:
            return node
        if x < node.key:
            node.left = self._delete(node.left, x)
            return node
        elif x > node.key:
            node.right = self._delete(node.right, x)
            return node
        else:
            # 找到要删除的节点，分情况处理
            if self.is_leaf(node):  # 叶子节点情况
                return None
            elif node.left is None:  # 只有右子节点情况
                return node.right
            elif node.right is None:  # 只有左子节点情况
                return node.left
            else:  # 有两个子节点情况
                # 找到右子树的最小节点（后继节点）来替换当前节点的值
                successor = self.findMin(node.right)
                node.key = successor.key
                # 在右子树中递归删除后继节点（已将值复制过来了）
                node.right = self._delete(node.right, successor.key)
                return node

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




# if __name__ == '__main__':


#     sp = BST()
#     seq1,op1,exist=getTaskSeq(existsLen=400000,seqLen=200000,taskFreq=[1,2,2])
#     seq0=exist
#     op0=[1 for i in range(len(seq0))]
#     # print(seq0,op0)
#     sp.seq_op(seq0, op0)
#     # print("前序遍历:")
#     # sp.preorder(sp.root)
#     # print()
#     # sp.preorder(sp.root)
#     # print()
#     # draw(sp.root)
#     sp.seq_op(seq1,op1)


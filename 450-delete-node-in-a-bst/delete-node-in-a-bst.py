class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None and root.right is None:
                root = None
            elif root.left is None:
                root = root.right
            elif root.right is None:
                root = root.left
            else:
                min_node = self._findMin(root.right)
                root.val = min_node.val

                root.right = self.deleteNode(root.right, min_node.val)
        
        return root
    
    def _findMin(self, root: TreeNode) -> TreeNode:
        while root.left:
            root = root.left
        return root

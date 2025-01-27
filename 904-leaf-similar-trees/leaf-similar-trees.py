class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getLeafSequence(root: Optional[TreeNode]) -> list:
            leaves = []
            if not root:
                return leaves
            if not root.left and not root.right:
                leaves.append(root.val)
            leaves.extend(getLeafSequence(root.left))
            leaves.extend(getLeafSequence(root.right))
            return leaves
        return getLeafSequence(root1) == getLeafSequence(root2)

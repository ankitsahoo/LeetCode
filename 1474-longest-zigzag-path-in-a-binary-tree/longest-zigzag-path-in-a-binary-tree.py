class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        self.max_length = 0
        
        def dfs(node, direction, length):
            if not node:
                return
            self.max_length = max(self.max_length, length)
            if direction == 'left':
                dfs(node.left, 'right', length + 1)
                dfs(node.right, 'left', 1)
            elif direction == 'right':

                dfs(node.right, 'left', length + 1)
                dfs(node.left, 'right', 1)

        dfs(root, 'left', 0)
        dfs(root, 'right', 0)
        
        return self.max_length
root = TreeNode(1)
root.right = TreeNode(1)
root.right.left = TreeNode(1)
root.right.left.left = TreeNode(1)
root.right.left.left.right = TreeNode(1)
solution = Solution()
print(solution.longestZigZag(root))  # Output: 3

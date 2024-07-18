from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # iterative
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right

        return result

    # recursive
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def helper(node):
          if not node:
              return
          helper(node.left)
          result.append(node.val)
          helper(node.right)

        helper(root)
        return result

root = TreeNode(1)
root_right = TreeNode(2)
root.right = root_right
root_right_left = TreeNode(3)
root_right.left = root_right_left

print(Solution().inorderTraversal(root))

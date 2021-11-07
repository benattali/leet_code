# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)

    def isMirror(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False

        return (
            node1.val == node2.val
            and self.isMirror(node1.left, node2.right)
            and self.isMirror(node1.right, node2.left)
        )


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)

root.left.left = TreeNode(3)
root.left.right = TreeNode(4)

root.right.left = TreeNode(4)
root.right.right = TreeNode(31)

print(Solution().isSymmetric(root))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def recurse(node, local_sum):
            if not (node.left or node.right):
                return local_sum + node.val == targetSum

            res =  False
            if node.left is not None:
                res |= recurse(node.left, local_sum + node.val)
            if node.right is not None:
                res |= recurse(node.right, local_sum + node.val)

            return res
        if root is None:
            return False
        return recurse(root, 0)

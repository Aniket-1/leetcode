#Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        sum = 0
        def calc(r, s):
            if r is None:
                return False
            if r.left==None and r.right==None:
                s += r.val
                if s==targetSum:
                    return True
                else:
                    return False
            return calc(r.left, s+r.val) or calc(r.right, s+r.val)
        
        if root is None:
            return False
        if (calc(root, sum)):
            return True
        return False

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        else:
            return self.check(root.left, root.right)
        
    def check(self, leftsub, rightsub):
        if not leftsub and not rightsub:
            return True
        elif not leftsub or not rightsub:
            return False
        else:
            return leftsub.val == rightsub.val and self.check(leftsub.left, rightsub.right) and self.check(leftsub.right, rightsub.left)

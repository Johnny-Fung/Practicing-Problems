# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        def helper(node, level):
            if len(levels)==level:
                levels.append([])
            levels[level].append(node.val)
            if node.left:
                helper(node.left,level+1)
            if node.right:
                helper(node.right,level+1)
        helper(root,0)
        return levels
    
    # len(levels) = level that we are currently on (traversing)
    # level = the level of the new node
    # len(levels)==level means current level we're looking at is same as level of new node, so we need to add new list (since levels counts from 1 behind, level of new node shoudl be 1 level ahead of len(levels))
    # Since helper function call is the node to be added,
    # We know we need to add a new empty list to move our "current level" to a new level whenever we're still on the previous level: len(levels)==level
    # think of it as, we're currently at a level (denoted as len(level)), we have a new node to add that is in a new level, so we need to make a new level for it

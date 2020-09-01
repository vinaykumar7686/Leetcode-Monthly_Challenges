Path Sum III
'''
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def __init__(self):
        self.total = 0
    def pathSum(self, root: TreeNode, target: int) -> int:
        if not root:
            return 0
        
        self.trav(root, 0, target)
        self.pathSum(root.left, target)
        self.pathSum(root.right, target)
    
        return self.total
        
    def trav(self, root, currsum, targetsum):
        if not root:
            return
        
        s = currsum+root.val
        if s==targetsum:
            self.total+=1
            print(root.val)
        
        self.trav(root.left, s, targetsum)
        self.trav(root.right, s, targetsum)
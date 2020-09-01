# Sum of Left Leaves

'''
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        s = 0
        stack = [root]
        
        while stack:
            node = stack.pop(0)
            
            if node.left!=None:
                stack.append(node.left)
                if not node.left.left and not node.left.right:
                    s=s+node.left.val
            if node.right!=None:
                stack.append(node.right)
        return s
        
        
                        
        
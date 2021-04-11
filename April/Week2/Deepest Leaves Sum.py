# Deepest Leaves Sum

'''
Given the root of a binary tree, return the sum of values of its deepest leaves.
 

Example 1:


Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
Example 2:

Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 100
   Hide Hint #1  
Traverse the tree to find the max depth.
   Hide Hint #2  
Traverse the tree again to compute the sum required.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.d = 0
        self.s = 0
        
    def deepestLeavesSum(self, root: TreeNode) -> int:
        
        def recur(dpth, ptr):
            if not ptr:
                return
            
            elif not ptr.left and not ptr.right:
                if dpth == self.d:
                    self.s+=ptr.val
                elif dpth > self.d:
                    self.s = ptr.val
                    self.d = dpth
                    
            else:
                recur(dpth+1, ptr.left)
                recur(dpth+1, ptr.right)
                
        recur(0, root)
        return self.s
            

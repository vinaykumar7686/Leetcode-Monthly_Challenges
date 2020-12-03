# Increasing Order Search Tree

'''
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

 

Example 1:


Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
Example 2:


Input: root = [5,1,7]
Output: [1,null,5,null,7]
 

Constraints:

The number of nodes in the given tree will be in the range [1, 100].
0 <= Node.val <= 1000
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    def increasingBST(self, root: TreeNode) -> TreeNode:
        arr = []
        
        def func(root):
            if not root:
                return
            
            if root.left:
                func(root.left)
                
            arr.append(root.val)
            
            if root.right:
                func(root.right)
                
                
        def create(curr):
            for num in arr:
                curr.right = TreeNode(num)
                curr = curr.right
                
            
        func(root)
        temp = TreeNode()
        create(temp)
        return temp.right
            
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        res = self.parent = TreeNode(None)
        def inorder(node):
            if node:
                inorder(node.left)
                node.left = None
                self.parent.right = node
                self.parent = node
                inorder(node.right)
        inorder(root)
        return res.right

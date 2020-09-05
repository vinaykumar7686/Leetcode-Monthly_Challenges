# All Elements in Two Binary Search Trees

'''
Given two binary search trees root1 and root2.

Return a list containing all the integers from both trees sorted in ascending order.

 

Example 1:


Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]
Example 2:

Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
Output: [-10,0,0,1,2,5,7,10]
Example 3:

Input: root1 = [], root2 = [5,1,7,0,2]
Output: [0,1,2,5,7]
Example 4:

Input: root1 = [0,-10,10], root2 = []
Output: [-10,0,10]
Example 5:


Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]
 

Constraints:

Each tree has at most 5000 nodes.
Each node's value is between [-10^5, 10^5].
   Hide Hint #1  
Traverse the first tree in list1 and the second tree in list2.
   Hide Hint #2  
Merge the two trees in one list and sort it.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1, root2):
        def inorder(root, lst):
            if not root: return
            inorder(root.left, lst)
            lst.append(root.val)
            inorder(root.right, lst)
        
        lst1, lst2 = [], []
        inorder(root1, lst1)
        inorder(root2, lst2)
        
        i1, i2, res = 0, 0, []
        s1, s2 = len(lst1), len(lst2)
        
        while i1 < s1 and i2 < s2:
            if lst1[i1] < lst2[i2]:
                res += [lst1[i1]]
                i1 += 1
            else:
                res += [lst2[i2]]
                i2 += 1
                
        return res + lst1[i1:] + lst2[i2:]

    # Memory Efficient Version
    def getAllElements_MemoryEfficient(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        ans = []
        
        def trav(root):
            
            if not root:
                return
            stack = [root]
            vals = [root.val]
            
            while stack:
                temp = stack[0]
                stack.pop(0)
                
                if temp.right:
                    stack.append(temp.right)
                    vals.insert(0, temp.right.val)
                if temp.left:
                    stack.append(temp.left)
                    vals.insert(0, temp.left.val)
            return (vals)
                   
        if root1:
            ans = trav(root1)
        if root2 and ans:
            ans.extend(trav(root2))
        elif root2:
            return sorted(trav(root2))
        
        return sorted(ans)
                    
                
                
                
            
                    
                
        

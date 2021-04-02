# Palindrome Linked List

'''
Given the head of a singly linked list, return true if it is a palindrome.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
 

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 

Follow up: Could you do it in O(n) time and O(1) space?
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.st = []
        self.ts = []
        
    def isPalindrome(self, head: ListNode) -> bool:
        def recur(ptr):
            if not ptr:
                return
            
            self.st.append(ptr.val)
            recur(ptr.next)
            self.ts.append(ptr.val)
            
        recur(head)
        # print(self.st, self.ts)
        return self.st == self.ts

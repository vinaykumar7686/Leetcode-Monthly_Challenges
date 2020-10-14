# Sort List

'''

Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

 

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
        
    def get_mid(self, head):
        
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        mid = slow.next
        slow.next = None
        return mid
    
    def merge_sublists(self, left, right):
        dum_head = ListNode(-1)
        current = dum_head
        
        while left and right:
            if left.val<=right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
                
            current = current.next
        
        current.next = left if left else right
        
        return dum_head.next
        
        
    
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        mid = self.get_mid(head)
        
        left = self.sortList(head)
        right = self.sortList(mid)
        
        
        return self.merge_sublists(left, right)

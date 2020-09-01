# Reorder List

'''
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None:
            return
        
        arr = []
        curr = head
        while curr:
            arr.append(curr)
            curr = curr.next
        
        left = 0
        right = len(arr)-1
        
        last = head
        
        while left<right:
            arr[left].next = arr[right]
            left+=1
            
            if left == right:
                last = arr[right]
                break
            
            arr[right].next = arr[left]
            right-=1
            last = arr[left]
            
        if last:
            last.next = None
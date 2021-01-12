# Add Two Numbers

'''

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s = ListNode(0)
        ans = s
        carry = 0
        
        while l1 or l2:
            
            
            if l1 and l2:
                
                add = l1.val+l2.val+carry
                
                if add>9:
                    s.next = ListNode(add-10)
                    carry = 1
                else:
                    s.next = ListNode(add)
                    carry = 0
                    
                l1 = l1.next
                l2 = l2.next
                    
            elif l1:
                
                add = l1.val+carry
                
                if add>9:
                    s.next = ListNode(add-10)
                    carry = 1
                else:
                    s.next = ListNode(add)
                    carry = 0
                    
                l1 = l1.next
                
            else:
                
                add = l2.val+carry
                
                if add>9:
                    s.next = ListNode(add-10)
                    carry = 1
                else:
                    s.next = ListNode(add)
                    carry = 0
                    
                l2 = l2.next
                
            s = s.next
            
        if carry!=0:
            s.next = ListNode(carry)
            
        return ans.next

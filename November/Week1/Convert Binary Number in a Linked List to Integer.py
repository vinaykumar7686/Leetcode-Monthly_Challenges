# Convert Binary Number in a Linked List to Integer

'''
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

 

Example 1:


Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
Example 2:

Input: head = [0]
Output: 0
Example 3:

Input: head = [1]
Output: 1
Example 4:

Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
Output: 18880
Example 5:

Input: head = [0,0]
Output: 0
 

Constraints:

The Linked List is not empty.
Number of nodes will not exceed 30.
Each node's value is either 0 or 1.
   Hide Hint #1  
Traverse the linked list and store all values in a string or array. convert the values obtained to decimal value.
   Hide Hint #2  
You can solve the problem in O(1) memory using bits operation. use shift left operation ( << ) and or operation ( | ) to get the decimal value in one operation.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        if not head:
            return 0
        
        binval = 0
        i = 0
        
        temp = head
        
        while temp:
            
            if temp.val == 1:
                binval = (binval)<<1
                binval = binval|(1)
            elif temp.val == 0:
                binval = (binval)<<1
                
            i+=1
            temp = temp.next
            
            # print(binval)
            
        return binval

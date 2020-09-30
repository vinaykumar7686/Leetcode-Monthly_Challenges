# First Missing Positive

'''
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Follow up:

Your algorithm should run in O(n) time and uses constant extra space.

   Hide Hint #1  
Think about how you would solve the problem in non-constant space. Can you apply that logic to the existing space?
   Hide Hint #2  
We don't care about duplicates or non-positive integers
   Hide Hint #3  
Remember that O(2n) = O(n)
'''

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        for num in nums:
            num = int(num)
            if num>0 and num<=n:
                nums[num-1] = str(nums[num-1])
        
        for i, num in enumerate(nums):
            if type(num)==int:
                return i+1
        return n+1
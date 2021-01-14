# Minimum Operations to Reduce X to Zero

'''

You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it's possible, otherwise, return -1.

 

Example 1:

Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
Example 2:

Input: nums = [5,6,7,8,9], x = 4
Output: -1
Example 3:

Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 104
1 <= x <= 109
   Hide Hint #1  
Think in reverse; instead of finding the minimum prefix + suffix, find the maximum subarray.
   Hide Hint #2  
Finding the maximum subarray is standard and can be done greedily.'''

#------------------------------------------  TLE  ----------------------------------------------------
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        if sum(nums)<x:
            return -1
        
        if sum(nums) == x:
            return len(nums)
        
        def helper(i, nums, x):
            
            if x == 0:
                return i
            
            if x<0:
                return float('inf')
            
            if not nums:
                return float('inf')
            
            return min(helper(i+1, nums[1:], x-nums[0]), helper(i+1, nums[:len(nums)-1], x-nums[-1]))
        
        res = helper(0, nums, x)
        
        return -1 if res == float('inf') else res

# Find First and Last Position of Element in Sorted Array

'''

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109

'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        if not (nums[0]<=target and nums[-1]>=target):
            return [-1, -1]
        
        
        # Start Index
        res = [-1,-1]
        
        lo = 0
        hi = len(nums)-1
        mid = lo + (hi-lo)//2
        
        while lo<=hi:
            mid = lo + (hi - lo) // 2
            
            if nums[mid] == target:
                res[0] = mid
                hi = mid-1
                
            elif nums[mid] < target:
                lo = mid+1
            
            else:
                hi = mid-1
        
        # End Index
        lo = 0
        hi = len(nums)-1
        mid = lo + (hi-lo)//2
        
        while lo<=hi:
            mid = lo + (hi - lo) // 2
            
            if nums[mid] == target:
                res[1] = mid
                lo = mid+1
                
            elif nums[mid] < target:
                lo = mid+1
            
            else:
                hi = mid-1
        
            
        return res

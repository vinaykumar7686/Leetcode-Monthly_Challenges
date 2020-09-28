# Subarray Product Less Than K

'''
Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Note:

0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.
   Hide Hint #1  
For each j, let opt(j) be the smallest i so that nums[i] * nums[i+1] * ... * nums[j] is less than k. opt is an increasing function.
'''

'''
It is given that all numbers are natural, that is they are more or equal than 1. The idea is to use two pointers (or sliding window) approach, where at each moment of time we try to extend our window. Let us beg, end-1 be the beginning and end of our window (it means that if beg=end=0, our window is empty), P is current product of numbers in our window and out is our answer we need to return.

On each iteration, we extend our window by one number to the right: however we need to check first, that the product do not exceed k. So, we remove numbers from the beginning of our window, until product is less then k. Note also, that we can not have end < beg, so we break if it is the case: it means than our window becomes empty. Finally, we update out += end - beg + 1: this is number of subarrays ending with end with product less than k.

Complexity: time complexity is O(n), because on each step we increase either beg or end. Space complexity is O(1).
'''

class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        out, beg, end, P = 0, 0, 0, 1
        while end < len(nums):
            P *= nums[end]
            while end >= beg and P >= k:
                P /= nums[beg]
                beg += 1
            out += end - beg + 1
            end += 1
        return out
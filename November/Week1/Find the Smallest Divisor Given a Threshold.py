# Find the Smallest Divisor Given a Threshold
'''
Given an array of integers nums and an integer threshold, we will choose a positive integer divisor and divide all the array by it and sum the result of the division. Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

Each result of division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

It is guaranteed that there will be an answer.

 

Example 1:

Input: nums = [1,2,5,9], threshold = 6
Output: 5
Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1. 
If the divisor is 4 we can get a sum to 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2). 
Example 2:

Input: nums = [2,3,5,7,11], threshold = 11
Output: 3
Example 3:

Input: nums = [19], threshold = 5
Output: 4
 

Constraints:

1 <= nums.length <= 5 * 10^4
1 <= nums[i] <= 10^6
nums.length <= threshold <= 10^6
   Hide Hint #1  
Examine every possible number for solution. Choose the largest of them.
   Hide Hint #2  
Use binary search to reduce the time complexity.
'''

class Solution0:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        compute_sum = lambda x : sum([ceil(n / x) for n in nums])
        d = 1
        while compute_sum(d) > threshold:
            d += 1
        
        return d
        
class Solution1:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        compute_sum = lambda x : sum([ceil(n / x) for n in nums])
        
        # search boundaries for the divisor
        left, right = 1, 2
        while compute_sum(right) > threshold:
            left = right
            right <<= 1
        
        # binary search
        while left <= right:
            pivot = (right + left) >> 1
            num = compute_sum(pivot)

            if num > threshold:
                left = pivot + 1
            else:
                right = pivot - 1
        
        # at the end of loop, left > right,
        # compute_sum(right) > threshold
        # compute_sum(left) <= threshold
        # --> return left
        return left
        
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        compute_sum = lambda x : sum([ceil(n / x) for n in nums])
        
        # binary search
        left, right = 1, nums[-1]
        while left <= right:
            pivot = (right + left) >> 1
            num = compute_sum(pivot)

            if num > threshold:
                left = pivot + 1
            else:
                right = pivot - 1
        
        # at the end of loop, left > right,
        # compute_sum(right) > threshold
        # compute_sum(left) <= threshold
        # --> return left
        return left

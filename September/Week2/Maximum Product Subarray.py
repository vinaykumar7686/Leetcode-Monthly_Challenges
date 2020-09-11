# Maximum Product Subarray

'''

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
	'''
	First, zeros are breaking any product chains that we may have so we only need to figure out the solution 
	for contiguos sequences without 0. Second, since we are dealing with integers the absolute value 
	of the running product will either increase or stay the same. As we iterate through array if 
	we encounter a number which turns our running_product negative we can use the earliest
	 seen negative product to make the running_product positive by dividing the running_product
 	by leftmost_negative. That's it.
	'''

        if not nums:
            return 0
        
        maxpro = nums[0]
        lneg = None
        pro = 1
        
        for num in nums:
            
            if not num:
                maxpro = max(maxpro, num)
                lneg = None
                pro = 1
                
                continue
                
            pro*=num
            
            if pro<0:
                if lneg:
                    maxpro = max(maxpro, pro//lneg)
                else:
                    lneg = pro
            else:
                maxpro = max(maxpro, pro)
                
        return maxpro
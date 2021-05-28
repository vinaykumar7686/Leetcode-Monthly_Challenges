# Maximum Erasure Value

'''

You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).

 

Example 1:

Input: nums = [4,2,4,5,6]
Output: 17
Explanation: The optimal subarray here is [2,4,5,6].
Example 2:

Input: nums = [5,2,1,2,5,2,1,2,5]
Output: 8
Explanation: The optimal subarray here is [5,2,1] or [1,2,5].
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 104
   Hide Hint #1  
The main point here is for the subarray to contain unique elements for each index. Only the first subarrays starting from that index have unique elements.
   Hide Hint #2  
This can be solved using the two pointers technique

'''

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res,s,e = 0,0,0
        add = 0
        return 1
        for i in range(len(nums)):
            
            if nums[i] not in nums[s:i]:
                add = add+nums[i]
                print('if')
                
            else:
                s = s+nums[s:i].index(nums[i])+1
                add = sum(nums[s:i+1])
                print('else')
            
            
            e = i
            
            res = max(res,add)
            print(s,e,add, res)
            
        return res

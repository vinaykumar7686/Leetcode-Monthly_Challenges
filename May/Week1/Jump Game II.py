# Jump Game II

'''
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
 

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 105
'''


'''
Intuition: from right to left, at every index in the array, what is the left most cell that can reach it? Example:

Input: [2,3,1,1,4]
Destination: index 4

If we traverse the array backwards from index 3 to 0, here are the indices to the left of our destination (index 4) that allows us to reach our destination (marked as True):
[--2----- 3-----1-----1] (array values)
[False, True, False, True] (can reach index 4?)

Algorithm:

At each destination (starting from len(nums) - 1), find the left most index that allows us to reach this destination. How do we know if the index we are at allows us to reach the destination? If the value at the current index is >= destinationIndex - currentIdx, then we can reach the destination
Increment the number of jump by 1 once we have found the left most position that can reach the current destination
Set the new destination to this left most index, and repeat
If the destination becomes 0, we are done
'''

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leftMost = dest = len(nums) - 1
        jump = 0
        while dest > 0:
        for i in range(dest - 1, -1, -1):
          if nums[i] >= dest - i:
            leftMost = i
        jump += 1
        dest = leftMost
        return jump


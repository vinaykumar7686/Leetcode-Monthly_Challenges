# Construct Target Array With Multiple Sums

'''
Given an array of integers target. From a starting array, A consisting of all 1's, you may perform the following procedure :

let x be the sum of all elements currently in your array.
choose index i, such that 0 <= i < target.size and set the value of A at index i to x.
You may repeat this procedure as many times as needed.
Return True if it is possible to construct the target array from A otherwise return False.

 

Example 1:

Input: target = [9,3,5]
Output: true
Explanation: Start with [1, 1, 1] 
[1, 1, 1], sum = 3 choose index 1
[1, 3, 1], sum = 5 choose index 2
[1, 3, 5], sum = 9 choose index 0
[9, 3, 5] Done
Example 2:

Input: target = [1,1,1,2]
Output: false
Explanation: Impossible to create target array from [1,1,1,1].
Example 3:

Input: target = [8,5]
Output: true
 

Constraints:

N == target.length
1 <= target.length <= 5 * 10^4
1 <= target[i] <= 10^9
   Hide Hint #1  
Given that the sum is strictly increasing, the largest element in the target must be formed in the last step by adding the total sum in the previous step. Thus, we can simulate the process in a reversed way.
   Hide Hint #2  
Subtract the largest with the rest of the array, and put the new element into the array. Repeat until all elements become one
'''

class Solution(object):
    def isPossible(self, target):
        """
        :type target: List[int]
        :rtype: bool
        """
        
        def findmax_s(nums):
            ans = float("-inf")
            loc = -1
            s = 0
            for i, j in enumerate(nums):
                if j>=ans:
                    ans = j
                    loc = i
                s+=j
                    
            return [ans, loc, s]
        
        n = len(target)
        
        while sum(target) > n:
            
            hi, loc , s = findmax_s(target)
            
            subs = hi-(s-hi)
            
            # print(hi, loc, s, subs)
            if subs<1:
                return False
            target[loc] = subs
            
        return True

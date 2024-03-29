# Maximum Points You Can Obtain from Cards


'''
There are several cards arranged in a row, and each card has an associated number of points The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

 

Example 1:

Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
Example 2:

Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.
Example 3:

Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.
Example 4:

Input: cardPoints = [1,1000,1], k = 1
Output: 1
Explanation: You cannot take the card in the middle. Your best score is 1. 
Example 5:

Input: cardPoints = [1,79,80,1,1,1,200,1], k = 3
Output: 202
 

Constraints:

1 <= cardPoints.length <= 10^5
1 <= cardPoints[i] <= 10^4
1 <= k <= cardPoints.length
   Hide Hint #1  
Let the sum of all points be total_pts. You need to remove a sub-array from cardPoints with length n - k.
   Hide Hint #2  
Keep a window of size n - k over the array. The answer is max(answer, total_pts - sumOfCurrentWindow)
'''
class Solution(object):
    def maxScore(self, nums, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        
        s = sum(nums)
        n = len(nums)
        
        rem = n-k
        
        
        temp = sum(nums[0:0+rem])
        val = temp
        
        for i in range(1, n-rem+1):
            temp = temp-nums[i-1]+nums[i+rem-1]
            if val>temp:
                val = temp
                
        return s-val

       
'''
# TLE Solutions

class Solution0(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        
        def rec(nums, i):
            if i<k and nums:
                return max(nums[0]+rec(nums[1:], i+1), nums[-1]+rec(nums[:-1], i+1))
            else:
                return 0
            
        return rec(cardPoints, 0)
       

class Solution1(object):
    def maxScore(self, nums, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        
        s = sum(nums)
        n = len(nums)
        
        rem = n-k
        
        val = float("inf")
        for i in range(0, n-rem+1):
            temp = sum(nums[i:i+rem])
            if val>temp:
                val = temp
                
        return s-val

'''

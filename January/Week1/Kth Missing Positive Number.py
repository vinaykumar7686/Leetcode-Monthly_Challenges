# Kth Missing Positive Number

'''
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.

 

Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
 

Constraints:

1 <= arr.length <= 1000
1 <= arr[i] <= 1000
1 <= k <= 1000
arr[i] < arr[j] for 1 <= i < j <= arr.length
   Hide Hint #1  
Keep track of how many positive numbers are missing as you scan the array.

'''

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        s = 0
        missings = 0
        for i in range(len(arr)):
            missings += arr[i]-s-1
            s = arr[i]
            
            # print(arr[i], missings)
            
            if missings>=k:
                break
            
        if missings>=k:
            return s+k-missings-1
        else:
            return s+k-missings
            

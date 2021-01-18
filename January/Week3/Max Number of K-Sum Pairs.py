# Max Number of K-Sum Pairs

'''
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

 

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= 109
   Hide Hint #1  
The abstract problem asks to count the number of disjoint pairs with a given sum k.
   Hide Hint #2  
For each possible value x, it can be paired up with k - x.
   Hide Hint #3  
The number of such pairs equals to min(count(x), count(k-x)), unless that x = k / 2, where the number of such pairs will be floor(count(x) / 2).
'''

# ------------------------------------------------------  TLE  -------------------------------------------------------------
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        hashmap = dict()
        res = 0
        
        for num in nums:
            
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
                
        
        pairs = set()
        
        for i in range(1, k//2+1):
            
            if not i in hashmap or not k-i in hashmap:
                continue
            pairs.add((i, k-i))
            
        pairs = list(pairs)
                          
        
        for i,j in pairs:
                
            if i == j:
                res += hashmap[i]//2
                hashmap[i] = hashmap[i]&1
            else:
                matched = min(hashmap[i], hashmap[j])
                res += matched
                
                hashmap[i] -=matched
                hashmap[j] -=matched
                
        return res

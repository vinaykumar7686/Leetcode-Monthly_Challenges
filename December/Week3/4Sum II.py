# 4Sum II

'''
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
'''

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        
        def helper(A, B, li = True):
            
            def createDict(nums):
                
                hashmap = dict()
                
                for num in nums:
                    if num in hashmap:
                        hashmap[num]+=1
                    else:
                        hashmap[num] = 1
                return hashmap
            
            dictA = createDict(A)
            dictB = createDict(B)
            dictAB = dict()
            
            for i in dictA:
                for j in dictB:
                    s = i+j
                    
                    if s in dictAB:
                        dictAB[s] = dictAB[s]+dictA[i]*dictB[j]
                    else:
                        dictAB[s] = dictA[i]*dictB[j]
                        
            # print(dictA, dictB, dictAB)
            return dictAB
        
        dictAB = helper(A,B)
        dictCD = helper(C,D)
        
        ans = 0
        for x in dictAB:
            if -x in dictCD:
                ans = ans + dictAB[x]*dictCD[-x]
                
        return ans
    
class TLE_Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        n = len(A)
        
        if n == 0:
            return 0
        
        arrs = [A,B,C,D]
        
        
        def helper(s, arrs):
            if not arrs:
                if s == 0:
                    return 1
                else:
                    return 0
            
            ans = 0
            for i in range(n):
                ans += helper(s+arrs[0][i], arrs[1:])
            return ans
        
        return helper(0, arrs)

# Numbers With Same Consecutive Differences

'''
Return all non-negative integers of length N such that the absolute difference between every two consecutive digits is K.

Note that every number in the answer must not have leading zeros except for the number 0 itself. For example, 01 has one leading zero and is invalid, but 0 is valid.

You may return the answer in any order.

 

Example 1:

Input: N = 3, K = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
Example 2:

Input: N = 2, K = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
 

Note:

1 <= N <= 9
0 <= K <= 9
'''
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = []
        
        if n==1:
            return [0,1,2,3,4,5,6,7,8,9]
        
        def solve(s, k, i, n):
            if len(s)==n:
                ans.append(s)
                return
            if i>9:
                return
                        
            if i+k<10:
                solve(s+str(i), k, i+k, n)
            if i-k>-1:
                solve(s+str(i), k, i-k, n)
            
        
        for i in range(1, 10):
            solve("", k, i, n)
        return list(set(ans))
            
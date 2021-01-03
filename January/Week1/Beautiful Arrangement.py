# Beautiful Arrangement

'''
Suppose you have n integers from 1 to n. We define a beautiful arrangement as an array that is constructed by these n numbers successfully if one of the following is true for the ith position (1 <= i <= n) in this array:

The number at the ith position is divisible by i.
i is divisible by the number at the ith position.
Given an integer n, return the number of the beautiful arrangements that you can construct.

 

Example 1:

Input: n = 2
Output: 2
Explanation: 
The first beautiful arrangement is [1, 2]:
Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).
Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).
The second beautiful arrangement is [2, 1]:
Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).
Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 15
'''

class Solution:
    def countArrangement(self, n: int) -> int:
        # using a recursive function we start from n and move towards 1 to ensure all elements are placed according to the condition
        #the 'used' array is used to keep track of the indices in which elements are placed
        used=[False for i in range(n+1)]
        self.res=0
        def recur_backtrack(x):
            if x==0:
                self.res+=1 #if we have placed all the elements
                return
            for i in range(1,n+1):
                if not used[i] and (x%i==0 or i%x==0): #if the index i is free and either i divides x or x divides i
                    used[i]=True
                    recur_backtrack(x-1) #Recursion for x-1 element to be placed
                    used[i]=False        #backtracking 
        recur_backtrack(n)
        return self.res

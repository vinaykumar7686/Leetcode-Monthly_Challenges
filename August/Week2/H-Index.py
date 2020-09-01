# H-Index
'''
Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:

Input: citations = [3,0,6,1,5]
Output: 3 
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had 
             received 3, 0, 6, 1, 5 citations respectively. 
             Since the researcher has 3 papers with at least 3 citations each and the remaining 
             two with no more than 3 citations each, her h-index is 3.
Note: If there are several possible values for h, the maximum one is taken as the h-index.

   Hide Hint #1  
An easy approach is to sort the array first.
   Hide Hint #2  
What are the possible values of h-index?
   Hide Hint #3  
A faster approach is to use extra space.
'''

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        li = [0]*(n+1)
        
        for citation in citations:
            if citation>n:
                li[n] = li[n]+1
            else:
                li[citation] =li[citation]+1
        s = 0
        ans = 0
        for freq, count in zip(li[::-1], range(n, -1, -1)):
            s = s+freq
            if s>=count:
                return count
        return 0
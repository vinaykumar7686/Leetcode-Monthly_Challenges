# Pascal's Triangle
'''
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
'''
class Solution:
    def getRow(self, k: int) -> List[int]:
        if k<0:
            return []
        if k == 0:
            return [1]
        
        ans = [1,1]
        prev = [1,1]
        for i in range(2,k+2):
            req = i-2
            # print(f'Total insertions needed for {i} is : {req}')
            ans = [1,1]
            for i in range(1, req+1):
                # print('inserting')
                ans.insert(i, (prev[i-1]+prev[i]))
            prev = ans
        return ans
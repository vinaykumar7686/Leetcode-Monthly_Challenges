# Non-overlapping Intervals

'''
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.


Example 1:

Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
Example 2:

Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
Example 3:

Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 

Note:

You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
'''
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])        
        i = 1
        ans= 0
        
        n = len(intervals)
        while i<len(intervals):
            if intervals[i][0]<intervals[i-1][1]:
                if intervals[i][1]<intervals[i-1][1]:
                    intervals.pop(i-1)
                else:
                    intervals.pop(i)
                    
                i-=1
                ans+=1
            i+=1
        return ans
    '''
    class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        end_sort = sorted(intervals, key=lambda x:x[1])
        last = None
        ans = 0
        for it in end_sort:
            if not last:
                last = it
            else:
                if it[0] >= last[1]:
                    last = it
                else:
                    ans += 1
        return ans
    '''
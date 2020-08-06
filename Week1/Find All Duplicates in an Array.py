# Find All Duplicates in an Array
'''

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]

'''
class Solution:
    def findDuplicates(self, arr: List[int]) -> List[int]:
        res = []
        for i, num in enumerate(arr):
            if arr[abs(num)-1]<0:
                res.append(abs(num))
            else:
                arr[abs(num)-1] = -1*abs(arr[abs(num)-1])
        return res
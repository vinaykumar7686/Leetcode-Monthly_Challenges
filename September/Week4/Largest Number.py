# Largest Number

'''
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
'''

class Solution_Efficient:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(x, y):
            u = x + y
            v = y + x
            if u == v:
                return 0
            elif u < v:
                return -1
            else:
                return 1

        v = map(str, nums)
        result = ''.join(reversed(sorted(v, key=cmp_to_key(cmp))))
        if result and result[0] == '0':
            return '0'
        else:
            return result

class My_Solution:
    def largestNumber(self, nums):
        nums = list(map(str, nums))
        def func(x,y):
            return x+y>y+x
        
        for x in range(len(nums)-1):
            
            y = x+1
            
            while x<len(nums) and y<len(nums):
                if not func(nums[x], nums[y]):
                    nums[x], nums[y] = nums[y], nums[x]
                y+=1
                    
        if nums[0]=="0":
            return "0"
        ans = "".join(nums)
        return ans

'''
# Default Solution
class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
        
class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num
'''


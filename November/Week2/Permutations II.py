# Permutations II

'''
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
'''
class MySolution:
        
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
                    
        def permute( nums, i, n):
            
            if i>=n-1:
                if nums not in ans:
                    ans.append(nums[::1])
                    # print(ans)
            else:
                
                for j in range(i, n):
                    nums[i], nums[j] = nums[j], nums[i]
                    permute(nums, i+1, n)
                    nums[i], nums[j] = nums[j], nums[i]
        permute(nums, 0, len(nums))
        return ans
                    
                
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        def backtrack(comb, counter):
            if len(comb) == len(nums):
                # make a deep copy of the resulting permutation,
                # since the permutation would be backtracked later.
                results.append(list(comb))
                return

            for num in counter:
                if counter[num] > 0:
                    # add this number into the current combination
                    comb.append(num)
                    counter[num] -= 1
                    # continue the exploration
                    backtrack(comb, counter)
                    # revert the choice for the next exploration
                    comb.pop()
                    counter[num] += 1

        backtrack([], Counter(nums))

        return results

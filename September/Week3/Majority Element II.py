# Majority Element II

'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
   Hide Hint #1  
How many majority elements could it possibly have?
'''

'''
Approach Details:
Boyer-Moore Voting Algorithm
Intuition

If we had some way of counting instances of the majority element as +1+1 and instances of any other element as -1−1, 
summing them would make it obvious that the majority element is indeed the majority element.

Algorithm

Essentially, what Boyer-Moore does is look for a suffix sufsuf of nums where suf[0]suf[0] is the majority element in that suffix. 
To do this, we maintain a count, which is incremented whenever we see an instance of our current candidate for majority element 
and decremented whenever we see anything else. Whenever count equals 0, we effectively forget about everything in nums up to the 
current index and consider the current number as the candidate for majority element. It is not immediately obvious why we can get 
away with forgetting prefixes of nums - consider the following examples (pipes are inserted to separate runs of nonzero count).

[7, 7, 5, 7, 5, 1 | 5, 7 | 5, 5, 7, 7 | 7, 7, 7, 7]

Here, the 7 at index 0 is selected to be the first candidate for majority element. count will eventually reach 0 after index 5 is 
processed, so the 5 at index 6 will be the next candidate. In this case, 7 is the true majority element, so by disregarding this 
prefix, we are ignoring an equal number of majority and minority elements - therefore, 7 will still be the majority element in the
 suffix formed by throwing away the first prefix.

[7, 7, 5, 7, 5, 1 | 5, 7 | 5, 5, 7, 7 | 5, 5, 5, 5]

Now, the majority element is 5 (we changed the last run of the array from 7s to 5s), but our first candidate is still 7. In this case,
 our candidate is not the true majority element, but we still cannot discard more majority elements than minority elements (this would
 imply that count could reach -1 before we reassign candidate, which is obviously false).

Therefore, given that it is impossible (in both cases) to discard more majority elements than minority elements, we are safe in discarding
 the prefix and attempting to recursively solve the majority element problem for the suffix. Eventually, a suffix will be found for which
 count does not hit 0, and the majority element of that suffix will necessarily be the same as the majority element of the overall array.

Complexity Analysis

Time complexity : O(n)O(n)

Boyer-Moore performs constant work exactly nn times, so the algorithm runs in linear time.

Space complexity : O(1)O(1)

Boyer-Moore allocates only constant additional memory.
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        n1, c1, n2, c2 = 'a',0,'a',0
        
        for num in nums:
            if c1 == 0 and n2!=num:
                n1 = num
                c1 = 1
            
            elif c2 == 0 and n1!=num:
                n2 = num
                c2 = 1
            
            elif n1==num:
                c1+=1
            
            elif n2==num:
                c2+=1
                
            else:
                c1-=1
                c2-=1
            #print(((n1,c1),(n2,c2)))
            
        ans = []
        
        for i in [n1,n2]:
            if nums.count(i)>n/3:
                ans.append(i)
        return list(set(ans))
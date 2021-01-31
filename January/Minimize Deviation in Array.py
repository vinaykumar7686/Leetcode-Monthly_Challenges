# Minimize Deviation in Array

'''
You are given an array nums of n positive integers.

You can perform two types of operations on any element of the array any number of times:

If the element is even, divide it by 2.
For example, if the array is [1,2,3,4], then you can do this operation on the last element, and the array will be [1,2,3,2].
If the element is odd, multiply it by 2.
For example, if the array is [1,2,3,4], then you can do this operation on the first element, and the array will be [2,2,3,4].
The deviation of the array is the maximum difference between any two elements in the array.

Return the minimum deviation the array can have after performing some number of operations.

 

Example 1:

Input: nums = [1,2,3,4]
Output: 1
Explanation: You can transform the array to [1,2,3,2], then to [2,2,3,2], then the deviation will be 3 - 2 = 1.
Example 2:

Input: nums = [4,1,5,20,3]
Output: 3
Explanation: You can transform the array after two operations to [4,2,5,5,3], then the deviation will be 5 - 2 = 3.
Example 3:

Input: nums = [2,10,8]
Output: 3
'''
'''
We prove the following:
Observation. Suppose the largest odd factor of all numbers in nums is c. Then for any num in nums with factor c, the transformed list with minimal deviation would transform num into c.
Proof. Suppose after transformation, the list contains three kinds of elements:

Small = {elements smaller than c};
Equal = {c};
Large = {elements larger than c}.
We then know all elements in Large are even numbers. (Otherwise c is not the largest odd factor!) Then we divide into two cases:

If Small is not empty: in this case c is not the smallest element. Then lifting c will not improve the deviation;
If Small is empty: in this case c is the smallest element, so lifting c to 2*c might improve the deviation; however, after lifting c to 2*c, all the elements in the list would be even numbers, so we can improve the deviation by dividing each element by 2. Then 2*c falls to c again.
Thus we finish the proof. With this intuition, we can transform the problem into a much easier one.

For each element num in nums and its candidate tranformations, we pick the transformations that are closest to c from upside and downside, and write as (x, y). When both directions are possible, x and y are both positive integers; otherwise one of them is set as infty. Then the problem becomes the following:

New problem: Suppose we have a list of positive integer pairs(including infty) [(x1, y1), ..., (xn, yn)]. We can pick either xi or yi from each pair, and the goal is to minimize max(picked xi's) + max(picked yi's).
This new problem is much easier: we can sort the list by values of xi, and maintain a running maximal value of yi's we have seen. See the codes for details.

Complexity: Computing the [(x1, y1), ..., (xn, yn)] list requires O(N log(M)) where M=max(nums); sorting requires O(N log(N)). So the overall complexity is O(N log(MN)), which is an improvement over the algorithms provided in the official solution.

Python code:
'''
    def minimumDeviation(self, nums: List[int]) -> int:
        # step 1: maximal odd factor
        max_odd = 0
        for i in nums:
            while i%2==0:i = i//2
            max_odd = max(max_odd, i)
            
        # step 2: calculating the [(xi, yi)] list
        dev = []
        for i in nums:
            if i%2 == 1:
                if 2*i>max_odd:
                    dev.append((2*i-max_odd, max_odd-i))
                else:
                    dev.append((float('inf'), max_odd-2*i))
            else:
                if i < max_odd:
                    dev.append((float('inf'), max_odd-i))
                else:
                    while i%2==0 and i>max_odd:
                        i = i//2
                    if i < max_odd:
                        dev.append((2*i-max_odd, max_odd-i))
                        
        # step 3: minimal sum of picked xi's and yi's
        dev.sort(reverse=True)
        if not dev: return 0
        max_down = [0] * len(dev)
        cur = 0
        for i in range(len(max_down)):
            cur = max(cur, dev[i][1])
            max_down[i] = cur
        mm = min(max_down[-1], dev[0][0])
        for i in range(len(max_down)-1):
            mm = min(mm, max_down[i]+dev[i+1][0])
        return mm

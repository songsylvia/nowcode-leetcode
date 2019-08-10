'''
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.
 

Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
 

Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
'''
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return True
        a = sum(nums)
        if a%2 !=0:
            return False
        a = a//2
        dp = [a+1 for i in range(a+1)]
        #体积为a的背包看是否能装满（每个物体只有一个0-1背包问题）如果值>数组长度说明不行
        dp[0] = 0
        for i in range(len(nums)):
            for j in range(a,nums[i]-1,-1):
                dp[j] = min(dp[j],dp[j-nums[i]]+1)
        if dp[a]>len(nums):
            return False
        else:
            return True
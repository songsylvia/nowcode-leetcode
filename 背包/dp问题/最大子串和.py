'''
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.


'''
#时间复杂度为O(N),空间复杂度O(N)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [0]*len(nums)
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            dp[i] = max(dp[i-1]+nums[i],nums[i])
        return max(dp)

    def  maxSubArray(self,nums):
    	if not nums:
    		return 0
    	loc = glo= nums[0]
    	for i in range(1,len(nums)):
    		loc = max(loc+nums[i],nums[i])
    		glo = max(loc,glo)
    	return glo
    	

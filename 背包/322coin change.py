'''
给定一组硬币，给定金额，问最少能组成金额的硬币数
Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1

[分析]
完全背包问题，但不是最大值，是最小值。
初始化时除了dp[0] = 0,其他初始化为dp[amount+1]
dp[j] = min(dp[j],dp[j-coins[i]]+1)
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins or amount<0:
            return -1
        #完全背包问题
        dp = [(amount+1) for i in range(amount+1)]
        dp[0] = 0
        for i in range(len(coins)) :
            for j in range(coins[i],amount+1):
                dp[j] = min(dp[j],dp[j-coins[i]]+1)
        return dp[amount] if dp[amount]<amount+1 else -1
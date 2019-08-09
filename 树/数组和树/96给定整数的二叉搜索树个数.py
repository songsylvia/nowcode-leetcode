class Solution:
    def numTrees(self, n: int) -> int:
        if n ==0 or n==1:
            return 1
        #其中dp[i]表示有i个数组成二叉树的个数
        dp = [0]*(n+1)
        dp[1],dp[0] = 1,1#空树也有1个
        for i in range(2,n+1,1):
            for j in range(i):
                dp [i] +=dp[j]*dp[i-1-j]#左子树个数*右子树个数
        return dp[n]

    
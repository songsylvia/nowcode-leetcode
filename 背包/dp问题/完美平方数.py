class Solution:
    def numSquares(self, n: int) -> int:
        if n == 0:
            return 0
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] =1
        dp[2] = 2
        for i in range(1,n+1):

            temp = float("inf")
            j = 1
            #print(i,j)
            while(i-j*j>=0):
                temp = min(temp,dp[i-j*j]+1)
                j+=1
                #print(temp)
            dp[i] =temp
        return dp[n]
if __name__ == '__main__':
    a = Solution().numSquares(7929)
    print(a)

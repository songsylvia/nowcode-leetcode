class Solution:
    def maximalSquare(self, matrix) -> int:
        if not matrix :
            return None
        n = len(matrix)+1
        m = len(matrix[0])+1
        maxres = 0
        dp =[[0 for i in range(m)] for j in range(n)]####注意这里一定不能写成dp = [[0*m]*n],这样变成m维数组操做了n遍。每一次改变都是所有元素同时变
        print(dp)
        for i in range(1,n):
            print(i)
            for j in range(1,m):
                print(j)
                if matrix[i-1][j-1] =="1":
                    dp[i][j] = min(min(dp[i-1][j],dp[i][j-1]),dp[i-1][j-1])+1
                else:
                    dp[i][j] = 0
                maxres = max(maxres,dp[i][j])
                print(i,j,dp)
        return maxres*maxres

if __name__ == '__main__':
    matrix = [["1","0","1","0"],["1","0","1","1"],["1","0","1","1"],["1","1","1","1"]]
    a = Solution().maximalSquare(matrix)
    print(a)
class Solution:
    def wordBreak(self, s, wordDict):
        res = []
        self.dfs(s,wordDict,"",res)
        print(res)
        #return res
    def check(self,s,dic):
    	dp =[False for i in range(len(s)+1)]
    	dp[0] = True
    	for i in range(1,len(s)+1):
    		for j in range(i):
    			if dp[j] and s[j:i] in dic:
    				dp[i] = True
    	return dp[-1]
    def dfs(self,s,dic,path,res):
    	if self.check(s,dic):
    		if not s:
    			res.append(path[:-1])
    		for i in range(1,len(s)+1):
    			if s[:i] in dic:
    				self.dfs(s[i:],dic,path+s[:i]+" ",res)
if __name__ == '__main__':
	ss = "catsanddog"
	wordDict = ["cat", "cats", "and", "sand", "dog"]
	Solution().wordBreak(ss,wordDict)




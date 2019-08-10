'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
'''
'''
给定一个字符串 ss，将 ss 划分成若干部分，使得每一部分都是回文串。

请返回所有合法的划分方案

'''
'''需要三个函数：函数本身，递归函数，检查是否为回文数的函数'''


'''
这个版本更好
def partition(self, s):
    res = []
    self.dfs(s, [], res)
    return res
    
def dfs(self, s, path, res):
    if not s: # backtracking
        res.append(path)
    for i in xrange(1, len(s)+1):
        if self.isPar(s[:i]):
            self.dfs(s[i:], path+[s[:i]], res)
            
def isPar(self, s):
    return s == s[::-1]

'''    
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(s,[],res)
        return res
    def check(self,s):
        return s == s[::-1]
    def dfs(self,s,path,res):
        if not s:
            res.append(path[:])
        for i in range(1,len(s)+1):
            if self.check(s[:i]):
                path.append(s[:i])
                self.dfs(s[i:],path,res)
                path.pop()           

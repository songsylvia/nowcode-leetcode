'''
132. Palindrome Partitioning II
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:

Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

'''
class Solution:
    def minCut(self, s: str) -> int:
        if not len(s) or s ==s[::-1]:
            return 0
        n = len(s)
        cut =[n for i in range(n+1)]#表示前i个字符能切多少刀
        cut[0] = -1
        for i in range(n):#表示中心
            print(i)
            #奇数
            j = 0
            print(j)
            while i-j>=0 and i+j<n and s[i-j]==s[i+j]:
                cut[i+j+1] = min(cut[i-j]+1,cut[i+j+1])
                j+=1
            j= 1
            while i-j+1>=0 and i+j<n and s[i-j+1] ==s[i+j]:
                cut[i+j+1] = min(cut[i+j+1],cut[i-j+1]+1)
                j+=1
        return cut[n]
                
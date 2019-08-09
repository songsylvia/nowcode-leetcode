'''
Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def maxend(node):
            if not node:
                return 0
            left = maxend(node.left)
            right = maxend(node.right)
            self.max = max(self.max, left + node.val + right)
            return max(node.val + max(left, right), 0)
        self.max = float("-inf")
        maxend(root)
        return self.max
        
        '''
        maxres = float("-inf")
        def dfs(node):
            nonlocal maxres
            if not node:
                return 0
            l = max(0,dfs(node.left))
            r = max(0,dfs(node.right))
            maxres = max(maxres,l +node.val+r)
            return node.val+max(l,r)
        dfs(root)
        return maxres'''
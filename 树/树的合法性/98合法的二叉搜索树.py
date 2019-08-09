'''
Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValidBSThelp(root,float('-inf'),float('inf'))
    def isValidBSThelp(self,root,lower,upper):
        if not root:
            return True
        if root.val<=lower or root.val>= upper:
            return False
        return self.isValidBSThelp(root.left,lower,root.val)and self.isValidBSThelp(root.right,root.val,upper)
      
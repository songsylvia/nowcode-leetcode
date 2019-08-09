'''
Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        leftDepth = self.getlevel(root.left)
        rightDepth = self.getlevel(root.right)
        if leftDepth == rightDepth:
            #左子树为满二叉树
            return (1<<leftDepth) + self.countNodes(root.right)
        if leftDepth >rightDepth:
            return (1<<rightDepth) + self.countNodes(root.left)
    def getlevel(self,node):
        if not node:
            return 0
        level = 0
        while node:
            level +=1
            node = node.left
        return level
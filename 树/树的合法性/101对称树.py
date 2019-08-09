'''
For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isMirror(root,root)
        '''
        if root.left and not root.right:
            return False
        if root.right and not root.left:
            return False
        '''
    def isMirror(self,a,b):
        if (not a and not b):
            return True
        if (not a or not b):
            return False
        return (a.val == b.val) & self.isMirror(a.left,b.right) & self.isMirror(a.right,b.left)
        
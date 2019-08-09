'''
Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        '''
        左右子树不超过1,有两种写法
        '''
        def helper(node):
            if not node:
                return True,0
            left_b,left_h = helper(node.left)
            right_b,right_h = helper(node.right)
            if not left_b or not right_b:
                return False,-1
            if abs(right_h-left_h)>1:
                return False,-1
            return True, max(left_h,right_h)+1
        
        
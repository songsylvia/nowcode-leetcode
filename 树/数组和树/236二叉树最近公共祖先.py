'''
iven the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]


 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.


'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #如果root为null,返回null
        #如果root左子树包含p,右子树含有q，或者相反,那么root就为最近的节点
        #如果全在左子树或者右子树上，那么继续在左右子树上查找
        if (root==None or root ==p or root ==q):
            return root
        leftnode = self.lowestCommonAncestor(root.left,p,q)
        rightnode = self.lowestCommonAncestor(root.right,p,q)
        if leftnode and rightnode:
            return root
        else:
            return rightnode if leftnode==None else leftnode
        
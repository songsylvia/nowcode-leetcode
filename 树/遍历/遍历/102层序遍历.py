# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = [root]
        while(len(q)>0):
            res.append([node.val for node in q])
            newq = []
            for node in q:
                if node.left:
                    newq.append(node.left)
                if node.right:
                    newq.append(node.right)
            q = newq
        return res
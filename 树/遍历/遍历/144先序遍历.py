# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        res = []
        self.dfs(root,res)
        return res
    def dfs(self,root,res):
        res.append(root.val)
        if root.left:
            self.dfs(root.left,res)
        if root.right:
            self.dfs(root.right,res)

# iteratively
def preorderTraversal(self, root):
    stack, res = [root], []
    while stack:
        node = stack.pop()
        if node:
            res.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
    return res
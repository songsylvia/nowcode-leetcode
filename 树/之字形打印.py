class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        #思路奇数层从左往右添加子节点，偶数层从右往左添加子节点
        if not root:
            return []
        res = []
        nodes = [root]
        lvl = False
        while nodes:
            nxt = []
            if not lvl:
                res.append([node.val for node in nodes])
            else:
                res.append([node.val for node in nodes[::-1]])
            for node in nodes:
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            nodes = nxt
            lvl = not lvl     
        return res

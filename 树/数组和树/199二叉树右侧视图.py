'''
Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def rightSideView(self,root:TreeNode) -> List[int]:
        res = []
        stack = [(root,0)]
        while stack:
            node,level = stack.pop()
            if node:
                if len(res)<level+1:
                    res.append([])
                res[level].append(node.val)
                stack.append((node.right,level+1))
                stack.append((node.left,level+1))
        return [x[-1]for x in res]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        
        if n ==0:
            return []
        #if n ==1:
          #  return [[1]]
        def helper(left,right):
            if left>right:
                return [None]
            res = []
            for i in range(left,right+1):
                for l in helper(left,i-1):
                    for r in helper(i+1,right):
                        node = TreeNode(i)
                        node.left = l
                        node.right = r
                        res.append(node)
                        
            return res #if res else [None]
        return helper(1,n)

'''
Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
   '''
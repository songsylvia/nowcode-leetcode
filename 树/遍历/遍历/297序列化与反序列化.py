# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "#!"
        res = str(root.val)+"!"
        res +=self.serialize(root.left)
        res +=self.serialize(root.right)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        #借助队列的结构来反序列化
        if not data:
            return None
        strlist = data.split("!")
        return self._deser(strlist)
    
    def _deser(self,strlist):
        if len(strlist)<=0:
            return None
        val = strlist.pop(0)
        if val=="#":
            return None
        root = TreeNode(val)
        root.left = self._deser(strlist)
        root.right = self._deser(strlist)
        return root
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
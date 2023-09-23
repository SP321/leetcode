# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        res = []
        def dfs(node):
            if not node:
                res.append(".")
                return
            res.append(chr(node.val+1000))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return "".join(res)
        

    def deserialize(self, data):
        self.i = 0
        def dfs():
            if data[self.i] == ".":
                self.i += 1
                return None
            node = TreeNode(ord(data[self.i])-1000)
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
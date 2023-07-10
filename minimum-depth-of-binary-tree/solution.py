class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        layer=[root]
        c=1
        while True:
            newlayer=[]
            for x in layer:
                if not x.left and not x.right:
                    return c
                if x.left:
                    newlayer.append(x.left)
                if x.right:
                    newlayer.append(x.right)
            layer=newlayer
            c+=1
        return -1
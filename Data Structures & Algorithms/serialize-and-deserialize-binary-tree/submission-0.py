# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res=[]
        def df(root):
            if not root :
                res.append("N")
                return
            res.append(str(root.val))
            df(root.left)
            df(root.right)

        df(root)
        return ",".join(res)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        sp=data.split(",")
        self.i=0
        def df():
            if sp[self.i]=="N":
                self.i+=1
                return None
            node=TreeNode(int(sp[self.i]))
            self.i+=1
            node.left=df()
            node.right=df()
            return node
        return df()



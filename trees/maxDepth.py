#problem: 104

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Sol:
    def maxDepth(self,root:Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_subtree_ht=self.maxDepth(root.left)
        ryt_subtree_ht=self.maxDepth(root.right)

        return 1 + max(left_subtree_ht , ryt_subtree_ht)
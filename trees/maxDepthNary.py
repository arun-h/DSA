#559

class Node:
    def __init__(val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val=val
        self.children = children
class Sol:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        if not root.children:
            return 1
        return 1+max(self.maxDepth(c) for c in root.children)
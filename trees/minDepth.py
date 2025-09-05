#problem 111, find the shortest path from the root of B.T to the leaf node i.e., min depth

def minDepth(self,root):
    if root is None:
        return 0
    if root.left is None:
        return 1+minDepth(root.right)
    if root.right is None:
        return 1+minDepth(root.left)
    
    return 1+min(minDepth(root.left),minDepth(root.right))

#using BFS to solve

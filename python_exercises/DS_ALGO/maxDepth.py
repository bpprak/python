# Definition for a binary tree node.
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: Node) -> int:
        if(root is None):
            return 0 
        if(root.left is None and  root.right is None):
            return 1
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left,right)+1
    
def preorder(node):
    if(node is not None):
        print(node.data)
        preorder(node.left)
        preorder(node.right)
    
    
root = Node(4)
root.left = Node(5)
root.right = Node(6)
root.left.left = Node(7)

preorder(root)
#              4
#          /       \
#         5         6
#       /  \      /   \
#      7   None  None  None
#     / \
# None   None

depth = Solution()

print("Length is", depth.maxDepth(root))



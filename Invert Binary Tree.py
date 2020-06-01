'''
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''


#Code provide the time complexity of O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        queue=[root]
        while len(queue):
            current = queue.pop()
            if current is None:
                continue
            self.swapLeftandRight(current)
            queue.append(current.left)
            queue.append(current.right)
            
        return root
    def swapLeftandRight(self, root):
        root.left, root.right = root.right , root.left
            
            
        

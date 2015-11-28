'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
'''
'''
Method: recursion O(n) time O(n) space
'''
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if root.left and root.right: # if node has two children, choose shorter one
            return min(self.minDepth(root.right), self.minDepth(root.left)) + 1
        else: # choose a branch if node has
            return max(self.minDepth(root.right), self.minDepth(root.left)) + 1

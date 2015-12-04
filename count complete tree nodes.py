'''
Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
'''
'''
Method: iteration O(logn**2) time O(logn) space
'''
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        current = root
        while current:
            if self.depth(current.left) == self.depth(current.right):
                res += 2**(self.depth(current.left))
                current = current.right
            else:
                res += 2**(self.depth(current.right))
                current = current.left
        return res
                
    def depth(self, root): # from the definition of the complete tree, only need to explore left child to find max depth, O(n) time
        if not root:
            return 0
        return self.depth(root.left) + 1
'''
Improvement
'''
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        current = root
        curDepth = self.depth(current) # record depth of current node, so we only need to check depth of right child
        while current:
            rightDepth = self.depth(current.right)
            if curDepth == rightDepth + 1:
                res += 2 ** (curDepth - 1)
                current = current.right
            else:
                res += 2 ** rightDepth
                current = current.left
            curDepth -= 1
        return res
        
        
    def depth(self, root):
        if not root:
            return 0
        return self.depth(root.left) + 1
